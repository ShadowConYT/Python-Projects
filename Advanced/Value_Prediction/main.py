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
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, random_state=42, test_size=0.2)
    print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

    # Load the Model
    model = LinearRegression()
    model.fit(X_train, Y_train)
    y_pred = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for Accuracy
    y_test_pred = model.predict(X_test)

    if plot:
        display_plots(inputs, outputs, y_line)

    return Prediction(value=y_pred[0][0], 
                        r2_score=r2_score(Y_test, y_test_pred),
                        slope = model.coef_[0][0],
                        intercept=model.intercept_[0],
                        mean_absolute_error=mean_absolute_error(Y_test, y_test_pred))

def display_plots(inputs, outputs, y_line):
    plt.title('Linear Regression')
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.plot(inputs, y_line, color='black')
    plt.show()

def main():
    years = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    salaries = [1000, 800, 2000, 10_000, 3400, 0, 4000, 3800, 5000, 4800]
    prediction = make_predictions(years, salaries, 75.5)
    print(prediction)

if __name__ == "__main__":
    main()