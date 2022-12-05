from typing import final
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text, func
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime
import pymysql
import pymysql.cursors

import pandas as pd

import db.config as config

DB_ADDRESS = config.DB_ADDRESS
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD


def get_db_connection():
  conn = pymysql.connect(host=DB_ADDRESS, port=3306, user=DB_USER,password=DB_PASSWORD, 
                         db='webtoon_info', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
  return conn

def get_alchemy_connection():
  db_data = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_ADDRESS + ':3306/' \
       + '' # schema이름
  engine = create_engine(db_data)
  return engine

def create_database():
    # TODO : 데이터베이스를 생성합니다.
    conn = pymysql.connect(host=DB_ADDRESS, port=3306, user=DB_USER,password=DB_PASSWORD)
    cursor = conn.cursor()
    sql = "CREATE DATABASE model_info;"
    cursor.execute(sql)
    cursor.execute("USE model_info;")
    conn.commit()
    conn.close()

def create_tables(conn):
    _create_model_info_table(conn)
    conn.commit()


def _create_model_info_table(conn):
      with conn.cursor() as cursor:
        sql = '''
              CREATE TABLE model_info (
                model_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                model_name varchar(255),
                pickle_file varchar(255)
              )
        '''
        cursor.execute(sql)
        conn.commit()


def insert_basic_table(conn):
      with conn.cursor() as cursor:
        sql = '''
              INSERT INTO model_info (model_name, pickle_file)
                VALUES (%s, %s)
        '''
        cursor.execute(sql)
        conn.commit()


# basic_info table 데이터 get
def get_basic_info_table(conn):
    with conn.cursor() as cursor:
      model_pkl = "select * from model_info"
      cursor.execute(model_pkl)
      model_pkl_info = cursor.fetchall()
    return model_pkl_info
