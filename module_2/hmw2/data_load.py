######## Data extraction #########
import logging
import os
import pandas as pd


class DataETLManager:
    def __init__(self, root_dir: str, csv_file: str):
        if os.path.exists(root_dir):
            if csv_file.endswith('.csv'):
                self.csv_file = os.path.join(root_dir, csv_file)
            else:
                logging.error('The file is not in csv format')
                exit(1)
        else:
            logging.error('The root dir path does not exist')
            exit(1)

        self.bos_crime_df = pd.read_csv(self.csv_file, sep=',', encoding='ISO-8859-1')
    def extract_data(self):
        """
        returns the boston crime data frame we hacve just created
        """
        return self.bos_crime_df

    def fetch_columns(self):
        """
        returns all the columns in the data
        """
        return self.bos_crime_df.columns.tolist()

    def data_description(self):
        """
        useful if we want a have a quick glance at the structure of the data

        """
        return self.bos_crime_df.describe()

    def fetch_categorical(self, categorical=False):
        """
        returns the categorical values in the data frame
        """
        if categorical:
            categorical_columns = list(set(self.bos_crime_df.columns) - set(self.bos_crime_df._get_numerical_data().columns))
            categorical_df = self.bos_crime_df[categorical_columns]
            return categorical_df
        else:
            non_categorical = list(set(self.bos_crime_df._get_numerical_data().columns))
            return self.bos_crime_df[non_categorical]
# def load_data(self):
#     database_config = {
#         'username': 'postgres',
#         'password': '17110303Cx',
#         'host': 'localhost',
#          'port':'5432',
#         'database':'postgres'
#         }

#     # create database connection using engine:
#      engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
#         database_config['username'],
#         database_config['password'],
#         database_config['host'],
#         database_config['port'],
#         database_config['database']
#         ))

#     data_to_load = type(pd.DataFrame())(self.bos_crime_df)
#     try:
#         data_to_load.to_sql('Credit Scoring', con=engine, if_exists='append', index=False)
#     except Exception as err:
#         print(err)


   