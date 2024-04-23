import os

import pandas as pd

from src.pipeline.prediction import custom_final_df
from src.utils import load_object

pkl_file_path = os.path.join("artifacts", "model.pkl")

#loading pickle file
model = load_object(pkl_file_path)


url = "https://chat.openai.com/"
custom_data = custom_final_df(url)
df = custom_data.final_df()

predict = model.predict(df)
print(df)
print(predict)