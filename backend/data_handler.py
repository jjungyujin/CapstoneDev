import pandas as pd
import numpy as np
import os
import utils

def make_merged_df(THICKNESS_PATH, MATERIAL_PATH, columns):
    thickness_folders = [i for i in os.listdir(THICKNESS_PATH)]
    thickness_folders = sorted(thickness_folders)

    material_folders = [i for i in os.listdir(MATERIAL_PATH)]
    material_folders = sorted(material_folders)
    
    # thickness dataframe
    thickness_df_all_years = pd.DataFrame()
    for thickness_file in thickness_folders:
        if thickness_file.startswith('2CRM'):
            thickness_df= pd.read_csv(THICKNESS_PATH+'/'+thickness_file, parse_dates=['TIME'])
            thickness_df_all_years = pd.concat([thickness_df_all_years, thickness_df])
        else:
            new_data_thickness_df = pd.read_csv(THICKNESS_PATH+'/'+thickness_file)
            new_data_thickness_df.columns = columns
            new_data_thickness_df['TIME'] = pd.to_datetime(new_data_thickness_df['TIME'], format="%Y-%m-%d %H:%M:%S")
            thickness_df_all_years = pd.concat([thickness_df_all_years, new_data_thickness_df])
    # 두께파일 전부 merge
    thickness_df_all_years = thickness_df_all_years.sort_values('TIME')
    thickness_df_all_years = thickness_df_all_years.reset_index(drop=True)

    # 자료 파일
    material_df_df_all_years = pd.DataFrame()
    for material_file in material_folders:
        if thickness_file.startswith('2CRM'):
            material_df= pd.read_csv(MATERIAL_PATH+'/'+material_file, parse_dates=['TIME'])
            material_df_df_all_years = pd.concat([material_df_df_all_years, material_df])
        else:
            new_data_material_df = pd.read_csv(MATERIAL_PATH+'/'+material_file, parse_dates=['TIME']).drop(['TIME_MS'], axis = 1)
            material_df_df_all_years = pd.concat([material_df_df_all_years, new_data_material_df])
    # 자료파일 전부 merge
    material_df_df_all_years = material_df_df_all_years.sort_values('TIME')
    material_df_df_all_years = material_df_df_all_years.reset_index(drop=True)

    # 두께 자료 파일 merge
    df_all_merge = pd.merge(thickness_df_all_years, material_df_df_all_years, how = 'inner', on='TIME')
    df_all_merge = df_all_merge[df_all_merge['PRC_CD'] == 'CR21'].reset_index(drop=True)
    df_all_merge = df_all_merge.drop(['Unnamed: 0'], axis = 1)
    return df_all_merge


def preprocessing_df(df_all_merge, thk_colums, jaryo_columns):
    coil_no_diff_idx = df_all_merge[df_all_merge['COIL_NO_x'] != df_all_merge['COIL_NO_y']].index
    
    df_all_merge = df_all_merge.drop(coil_no_diff_idx).drop('COIL_NO_y', axis = 1)
    df_all_merge = df_all_merge.rename(columns = {'COIL_NO_x' : 'COIL_NO'})

    df_all_merge.columns = df_all_merge.columns.map(lambda x: x[3:] if x.startswith('DK_') else x)

    df_all_merge['N2_AGC_DB222_DD154'] = df_all_merge['N2_AGC_DB222_DD154'].replace(0, np.NaN)
    df_all_merge['N2_AGC_DB222_DD154'] = df_all_merge['N2_AGC_DB222_DD154'].fillna(method = 'ffill')
    
    df_used_columns = thk_colums + jaryo_columns

    df_all_merge = df_all_merge[df_used_columns]
    
    return df_all_merge


def extract_vibration(df_all_merge): # method3 진행
    processed_list = []

    for name, value in df_all_merge.groupby('COIL_NO'):
        pass_no_list = value['PASS_NO'].unique()
        end_pass_no = pass_no_list[-1]
    
        if len(pass_no_list) > 1:
            end_idx = value[value['PASS_NO'] == end_pass_no].index[-1]
            processed_df = value.loc[:end_idx]
            processed_list.append(processed_df)

    processed_df = pd.concat(processed_list).reset_index(drop=True)
    
    time_series_col = pd.to_datetime(processed_df['TIME'], format="%Y-%m-%d %H:%M:%S")
    time_series_df = processed_df.copy()
    time_series_df['TIME'] = time_series_col
    time_series_df.set_index('TIME', inplace=True)
    
    thk_act_avg = time_series_df['EXIT_THK_ACT_AVG']
    thk_act_avg_shift = thk_act_avg.shift(periods=1, fill_value=0)
    thk_act_avg_compare = abs(thk_act_avg_shift - thk_act_avg)

    time_series_df['THK_ACT_AVG_CHANGE_AMT'] = thk_act_avg_compare

    less_change_df = time_series_df[(time_series_df['THK_ACT_AVG_CHANGE_AMT'] > 0.001) & (time_series_df['THK_ACT_AVG_CHANGE_AMT'] < 0.05)]
    less_change_df['TIME'] = less_change_df.index
    less_change_df.reset_index(inplace=True, drop=True)
    
    name_list = []
    for name, value in less_change_df.groupby(['COIL_NO', 'PASS_NO']):
        name_list.append(name)

    coil_checklist = []
    for name, value in processed_df.groupby(['COIL_NO', 'PASS_NO']):
        if name not in name_list:
            coil_checklist.append(name[0])
    
    outlier_coil = coil_checklist[1:]
    drop_idx = less_change_df[less_change_df['COIL_NO'].isin(outlier_coil)].index
    less_change_df = less_change_df.drop(drop_idx, axis=0)
    less_change_df.reset_index(inplace=True, drop=True)

    pass2_coil_list = []
    for name, value in less_change_df.groupby(['COIL_NO']):
        if len(value['PASS_NO'].unique()) == 2:
            pass2_coil_list.append(name)

    drop_idx = less_change_df[less_change_df['COIL_NO'].isin(pass2_coil_list)].index
    less_change_df = less_change_df.drop(drop_idx, axis=0)
    less_change_df.reset_index(inplace=True, drop=True)
    
    less_change_df = less_change_df.drop('THK_ACT_AVG_CHANGE_AMT', axis = 1)

    return less_change_df
    

def make_final_df(vib_df, final_csv_path):
    select_df = pd.DataFrame(columns=vib_df.columns)
    coil_no_list = [i for i in vib_df.COIL_NO.unique()]
    
    for coil_no in coil_no_list:
        pass_list = vib_df[vib_df['COIL_NO'] == coil_no]['PASS_NO'].unique()
        for pass_no in pass_list:
           select_df = pd.concat([select_df, vib_df[(vib_df['COIL_NO'] == coil_no) & (vib_df['PASS_NO'] == pass_no)].sample(n=10)])
    
    sampled_dfs = []
    for coil in coil_no_list:
        sampled_dfs.append(select_df[select_df['COIL_NO'] == coil])

    final_df = pd.DataFrame()

    for sampled_df in sampled_dfs:
        sampled_pass_dfs = []
        for name, df in sampled_df.groupby(['PASS_NO']):
            sampled_pass_dfs.append(df)

        multiplied_merge_df = pd.DataFrame()

        for i in range(len(sampled_pass_dfs)-1):
            pass1_df = sampled_pass_dfs[i].reset_index(drop=True)
            pass2_df = sampled_pass_dfs[i+1][['PASS_NO', 'EXIT_THK_ACT_AVG']].reset_index(drop=True)
            pass2_df.columns = ['PASS_NO_y', 'EXIT_THK_ACT_AVG_y']
            multiplied_df = pd.concat([pass1_df, pass2_df], axis = 1)
            multiplied_merge_df = pd.concat([multiplied_merge_df, multiplied_df], axis = 0)
        final_df = pd.concat([final_df, multiplied_merge_df], axis = 0)

    final_df = final_df.drop(['COIL_NO', 'PASS_NO', 'PASS_NO_y','TIME'], axis = 1)
    final_df = final_df.rename(columns = utils.rename_dict)
    final_df = final_df[utils.used_columns]
    
    if 'Unnamed: 0' in final_df.columns:
        final_df = final_df.drop(['Unnamed: 0'], axis=1)
    
    final_df.to_csv(f'{final_csv_path}/final_df.csv')

    return final_df