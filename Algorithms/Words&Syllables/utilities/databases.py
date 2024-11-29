import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def getEngine():
    host = ''
    database = ''
    username = ''
    password = ''
    port = ''

    connectionString = f'postgresql://{username}:{password}@{host}:{port}/{database}'

    engine = create_engine(connectionString)

    return engine


def getData(query):
    data = None

    try:
        data = pd.read_sql(query, getEngine())
    except SQLAlchemyError as ex:
        print(ex)

    return data
