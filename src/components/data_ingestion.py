import os
import sys
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass

class DataIngestionConfig:
    '''
        paths are defined related to the data we are using the program this manages the path.
    '''
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str =os.path.join('artifacts',"test.csv")
    raw_data_path : str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
         self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        '''
            The actual ingestion of data taking place here.
        '''
        logging.info("Enter the data ingestion method or component")
        try:
            # taking data from the local this can we change furtur
            df=pd.read_csv("/home/info/Desktop/ml_project/notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            logging.info("Train test split initialized")
            train_set,test_set = train_test_split(df,test_size = 0.2,random_state = 42)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False,header = True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj2 = DataTransformation()
    obj.initiate_data_ingestion()
    obj2.initiate_data_transformation("/home/info/Desktop/ml_project/artifacts/train.csv","artifacts/test.csv")