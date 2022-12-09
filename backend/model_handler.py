import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor as xgb
from lightgbm import LGBMRegressor as lgb
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error

def make_dataset(final_df):
    if 'Unnamed: 0' in final_df.columns:
        final_df = final_df.drop(['Unnamed: 0'], axis=1)

    df_X = final_df.drop('EXIT_THK_ACT_AVG', axis = 1)
    df_y = final_df['EXIT_THK_ACT_AVG']

    train_val_X, test_X, train_val_y, test_y = train_test_split(df_X, df_y, test_size=0.2, random_state=42)

    return train_val_X, test_X, train_val_y, test_y


def _xgb(learning_rate = 0.01, max_depth = 6, n_estimators = 300):
    model = xgb(learning_rate = learning_rate, max_depth= max_depth, n_estimators= n_estimators)
    return model


def save_model(model, train_X, train_y, model_path):
    model.fit(train_X, train_y)
    joblib.dump(model, f'{model_path}/saved_model.pkl')
    
    return f'{model_path}/saved_model.pkl'


def predict_value(model_path, input_list, train_columns):
    model_file = [model_path + '/' + i for i in os.listdir(model_path)][0]
    model = joblib.load(model_file)
    input_list = pd.DataFrame(data = [input_list], columns=train_columns)
    
    predict = model.predict(input_list)[0]
    return predict
