import pandas as pd
import data_handler

import config
import utils

THICKNESS_PATH = config.THICKNESS_PATH
MATERIAL_PATH = config.MATERIAL_PATH

thk_colums = utils.thk_colums
jaryo_columns = utils.jaryo_columns

def main():
    try:
        df_all_merge =  data_handler.make_merged_df(THICKNESS_PATH, MATERIAL_PATH)
        df_all_merge = data_handler.preprocessing_df(df_all_merge, thk_colums, jaryo_columns)
        df_all_merge.to_csv('../db/data/final_csv/df_all_merge.csv')
        # method 3 및 sampling, ML 코드 추가 필요
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()  