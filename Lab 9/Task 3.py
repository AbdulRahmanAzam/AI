from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import KFold
from sklearn.svm import SVC
df = pd.read_csv("customer_data.csv")
# display(df.head())
print(df.isnull().sum())

df = df.fillna(method="ffill")
print(df.isnull().sum())

  df = df.fillna(method="ffill")
kf = KFold(n_splits=5,shuffle=True,random_state=42)
y =df.pop("HighValue")
accuracy = []
scaler = StandardScaler()
df = scaler.fit_transform(df)
svm = SVC(kernel="rbf",C=1,gamma="scale")
for tr_idx,ts_idx in kf.split(df):
    X_train,X_test = df[tr_idx],df[ts_idx]
    Y_train,Y_test = y.iloc[tr_idx],y.iloc[ts_idx]
    
    svm.fit(X_train,Y_train)
    Y_pred = svm.predict(X_test)
    
    acc= accuracy_score(Y_pred,Y_test)
    accuracy.append(acc)
    
print(f"Final Accuracy Score: {np.mean(accuracy)}")
print("Confusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))
