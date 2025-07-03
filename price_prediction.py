import pickle
import pandas as  pd
import numpy as np
import joblib

# Load the pipeline model
# pipeline_xgb = joblib.load('Model/pipeline_xgb.pkl')

pipeline_xgb = joblib.load("Model/pipeline_xgb.joblib")

# Load the dataset
df = joblib.load('datasets/data.joblib')



columns = df.columns.tolist()[:-1]

def price_predictor(location, bhk, built_up_area, transaction, status,
                    totalfloor, furnishing, facing, bathroom, floor_category, luxury_category):
    data = [[location, bhk, built_up_area, transaction, status, totalfloor, furnishing, facing, bathroom, floor_category, luxury_category]]
    one_df = pd.DataFrame(data, columns=columns)
    
    base_price = np.expm1(pipeline_xgb.predict(one_df))[0]  # Replace with actual prediction logic
    low = base_price - 0.22
    high = base_price + 0.22
    
    return round(low, 2), round(high, 2)