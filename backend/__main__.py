import pandas as pd
import data_handler
import model_handler

import os
import config
import utils

THICKNESS_PATH = config.THICKNESS_PATH
MATERIAL_PATH = config.MATERIAL_PATH

thk_colums = utils.thk_colums
jaryo_columns = utils.jaryo_columns

FINAL_DF_PATH = config.FINAL_DF_PATH
MODEL_PATH = config.MODEL_PATH

def main():
    try:
        if os.path.exists(config.FINAL_DF_PATH):
            print('final_df.csv is already exists')
            file_name = os.listdir(config.FINAL_DF_PATH)[0]
            final_df = pd.read_csv(FINAL_DF_PATH+'/'+file_name)
        else:
            df_all_merge =  data_handler.make_merged_df(THICKNESS_PATH, MATERIAL_PATH, utils.columns)
            df_all_merge = data_handler.preprocessing_df(df_all_merge, thk_colums, jaryo_columns)
            
            vibration = data_handler.extract_vibration(df_all_merge)
            print('Successfully extract vibration data!')
            
            final_df = data_handler.make_final_df(vibration, config.FINAL_DF_PATH)
            print('final dataset is saved')
        
        train_val_X, test_X, train_val_y, test_y = model_handler.make_dataset(final_df)
            
        print('Training your Model!')
        model = model_handler._xgb()
        
        print('Fitting is Done!')
        _model_path = model_handler.save_model(model, train_val_X, train_val_y, MODEL_PATH)
        print('Successfully saved your model!')
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()  