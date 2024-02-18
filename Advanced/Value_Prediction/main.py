from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model import Prediction

def make_predictions(inputs: float, outputs: float, input_value: float, plot: bool = False):
    if len(inputs) != len(outputs):
        raise ValueError("Inputs and outputs must have the same length")
    
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the DataFrame to fit the model X,y
    X = np.array(df['inputs']).reshape(-1,1)
    y = np.array(df['outputs']).reshape(-1,1)

    # Split the Dataset
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, random_state=0, test_size=0.2)
