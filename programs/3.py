import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main():
    filename = "height_weight.csv"

    df = pd.read_csv(filename)
    X = df[['Height(Inches)']].values
    y = df['Weight(Pounds)'].values

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Take input from user
    height = float(input("Enter height (inches): "))

    new_data = np.array([[height]])
    prediction = model.predict(new_data)
    pr_weight = prediction[0]*0.454
    print(f"Predicted weight:", pr_weight, "kg")

    

while True:
    main()

