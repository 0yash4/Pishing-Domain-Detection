from src.exception import CustomException
from src.logger import logging

import pandas as pd
import sys
import os
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
        raw_data_path = os.path.join("artifacts", "dataset_full.csv")
        input_data_path = os.path.join("artifacts", "input_data.csv")
        output_data_path = os.path.join("artifacts", "output_data.csv")


class data_initailization:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the Data ingestion method or component")
        try:
            df=pd.read_csv('artifacts\dataset_full.csv')
            
            input_data = df.iloc[:, :-1]
            output_data = df.iloc[:, -1:]
            
            input_data.to_csv(self.ingestion_config.input_data_path, index = False)
            output_data.to_csv(self.ingestion_config.output_data_path, index = False)
            
            logging.info("Ingestion of data is completed.")
            
            return(
                self.ingestion_config.input_data_path,
                self.ingestion_config.output_data_path

            )
            
        except CustomException as e:
            raise CustomException(e, sys)
            

if __name__ == "__main__":
    obj=data_initailization()
    train_data, test_data = obj.initiate_data_ingestion()