from src.components import data_ingestion
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from src.components.data_ingestion import DataIngestionConfig

import os
import pandas as pd
import sys
import dill
import pickle
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV,cross_val_score

from sklearn.ensemble import RandomForestClassifier

@dataclass
class model_trainer_config:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    

class Modeltrainer:
    def __init__(self):
        self.model_trainer_config = model_trainer_config()
        self.ingestion_config = DataIngestionConfig()
        
    def model_trainer(self):
        try:
            models: dict = {
                "Random Forest" : RandomForestClassifier()
            }
            
            param_grid: dict = {
                "Random Forest": {'n_estimators': [200], 'max_depth': [None], 'min_samples_split': [2]},
            }
            
            result: dict = {}
            for name, model in models.item():
                gird_search = GridSearchCV(estimator=models, param_grid=param_grid[name], cv=5, scoring="accuracy")
                gird_search.fit(self.ingestion_config.input_file_path, self.ingestion_config.output_file_path)
                best_model = gird_search.best_estimator_
                best_params = gird_search.best_params_
                accuracy = cross_val_score(best_model, self.ingestion_config.input_file_path, 
                                        self.ingestion_config.output_file_path, cv=2, scoring='accuracy').mean()
                result[name] = {"Accuracy": accuracy, "Best Param": best_params}
                
            if accuracy < 0.6:
                raise CustomException("No best model found")
            else:
                logging.info(f"Best model found with the accuracy score of {accuracy}")
            
            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )
            
            return(
                accuracy
            )
            
        except CustomException as e:
            raise CustomException(e, sys)
            
        