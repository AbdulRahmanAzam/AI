import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,root_mean_squared_error,r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,KFold,LeaveOneOut
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
df = pd.read_csv("house_prices_dataset.csv")
display(df.head())

# display(df.info())

# print(df.isnull().sum())

df_encoded  = pd.get_dummies(df,columns=["Neighborhood"],drop_first=True)
display(df_encoded.info())

# Correct dummy encoding for the test sample
test_sample = {
    "SquareFootage": 2500,
    "Bedrooms": 4,
    "Bathrooms": 2.5,
    "HouseAge": 10,
    "Neighborhood": "Uptown"
}

# Convert to DataFrame
test = pd.DataFrame([test_sample])

#When Categorical Column Have Null Value
# df['Neighborhood'] = df['Neighborhood'].fillna(df['Neighborhood'].mode()[0])


# When Too many columns have NULL Values
# Or fill with forward-fill or backward-fill
# df = df.fillna(method='ffill')  # Forward fill
# df = df.fillna(method='bfill')  # Backward fill


# One-hot encode the test sample
test = pd.get_dummies(test, columns=["Neighborhood"], drop_first=True)

# Align test columns with training columns (fill missing columns with 0)
for col in df_encoded.columns:
    if col not in test.columns and col != "Price":
        test[col] = 0

# print(test)
# Reorder columns to match training data
test = test[df_encoded.drop(columns="Price").columns]
# print(test)
LR = LinearRegression()
y = df_encoded.pop("Price")
X_train,X_test,Y_train,Y_test = train_test_split(df_encoded,y,test_size=0.2,random_state=42)
LR.fit(X_train,Y_train)
Y_pred = LR.predict(X_test)

rmse = root_mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f"RMSE: {rmse}, R2 Score: {r2:.2f}")

predicted_price = LR.predict(test)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
