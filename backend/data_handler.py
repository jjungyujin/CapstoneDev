import pandas as pd
import numpy as np
import os

def make_merged_df(THICKNESS_PATH, MATERIAL_PATH, columns):
    thickness_folders = [THICKNESS_PATH + i for i in os.listdir(THICKNESS_PATH)]
    thickness_folders = sorted(thickness_folders)

    material_folders = [MATERIAL_PATH + i for i in os.listdir(MATERIAL_PATH)]
    material_folders = sorted(material_folders)
    
    # thickness dataframe
    thickness_df_all_years = pd.DataFrame()
    for thickness_file in thickness_folders:
        if thickness_file.startswith('2CRM'):
            thickness_df= pd.read_csv(thickness_file, parse_dates=['TIME'])
            thickness_df_all_years = pd.concat([thickness_df_all_years, thickness_df])
        else:
            new_data_thickness_df= pd.read_csv(thickness_file, parse_dates=['TIME'])
            new_data_thickness_df.columns = columns
            thickness_df_all_years = pd.concat([thickness_df_all_years, new_data_thickness_df])
    # 두께파일 전부 merge
    thickness_df_all_years = thickness_df_all_years.sort_values('TIME')
    thickness_df_all_years = thickness_df_all_years.reset_index(drop=True)

    # 자료 파일
    material_df_df_all_years = pd.DataFrame()
    for material_file in material_folders:
        if thickness_file.startswith('2CRM'):
            material_df= pd.read_csv(material_file, parse_dates=['TIME'])
            material_df_df_all_years = pd.concat([material_df_df_all_years, material_df])
        else:
            new_data_material_df = pd.read_csv(material_file, parse_dates=['TIME']).drop(['Unnamed: 0', 'TIME_MS'], axis = 1)
            material_df_df_all_years = pd.concat([material_df_df_all_years, new_data_material_df])
    # 자료파일 전부 merge
    material_df_df_all_years = material_df_df_all_years.sort_values('TIME')
    material_df_df_all_years = material_df_df_all_years.reset_index(drop=True)

    # 두께 자료 파일 merge
    df_all_merge = pd.merge(thickness_df_all_years, material_df_df_all_years, how = 'inner', on='TIME')
    df_all_merge = df_all_merge[df_all_merge['PRC_CD'] == 'CR21'].reset_index(drop=True)

    return df_all_merge


def preprocessing_df(df_all_merge, thk_colums, jaryo_columns):
    coil_no_diff_idx = df_all_merge[df_all_merge['COIL_NO_x'] != df_all_merge['COIL_NO_y']].index
    
    df_all_merge = df_all_merge.drop(coil_no_diff_idx).drop('COIL_NO_y', axis = 1)
    df_all_merge = df_all_merge.rename(columns = {'COIL_NO_x' : 'COIL_NO'})

    df_all_merge.columns = df_all_merge.columns.apply(lambda x: x[3:] if x.startswith('DK_') else x)

    df_all_merge['N2_AGC_DB222_DD154'] = df_all_merge['N2_AGC_DB222_DD154'].replace(0, np.NaN)
    df_all_merge['N2_AGC_DB222_DD154'] = df_all_merge['N2_AGC_DB222_DD154'].fillna(method = 'ffill')
    
    df_used_columns = thk_colums + jaryo_columns

    df_all_merge = df_all_merge[df_used_columns]
    
    return df_all_merge


def engineering_feature(df_all_merge_path): # method3 진행
    return True
    # all_df = pd.read_csv(df_all_merge_path).drop('Unnamed: 0', axis=1)
    # processed_list = []

    # for name, value in all_df.groupby('COIL_NO'):
    #     pass_no_list = value['PASS_NO'].unique()
    #     end_pass_no = pass_no_list[-1]
    
    #     if len(pass_no_list) > 1:
    #         end_idx = value[value['PASS_NO'] == end_pass_no].index[-1]
    #         processed_df = value.loc[:end_idx]
    #         processed_list.append(processed_df)

    # processed_df = pd.concat(processed_list).reset_index(drop=True)

    # last_exit_thk_info = []

    # for name, value in processed_df.groupby(['COIL_NO', 'PASS_NO']):
    #     last_exit_thk = value.iloc[-1]['EXIT_THK_ACT_AVG']
    #     coil_pass_thk = list(name)
    #     coil_pass_thk.append(last_exit_thk)
    #     last_exit_thk_info.append(coil_pass_thk)
    
    # last_exit_thk_df = pd.DataFrame(last_exit_thk_info, columns=['COIL_NO', 'PASS_NO', 'LAST_EXIT_THK'])
    # last_exit_thk_df['PASS_NO'] = last_exit_thk_df['PASS_NO'] + 1

    # method3_df = pd.merge(processed_df, last_exit_thk_df, on=['COIL_NO', 'PASS_NO'])