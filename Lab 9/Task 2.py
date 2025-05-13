from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score,precision_score
from sklearn.model_selection import KFold,train_test_split,LeaveOneOut
from sklearn.svm import SVC
df = pd.read_csv("synthetic_email_spam_dataset.csv")
# display(df.head())

# print(df.info())
df_encoded = pd.get_dummies(df,columns=["sender_domain"],drop_first=True)
# print(df_encoded.info())
# display(df_encoded.head())
# print(df.isnull().sum())
svm = SVC(kernel="rbf",C=1,gamma="scale")
y = df_encoded.pop("is_spam")
scalar = StandardScaler()
kf = KFold(n_splits=10,shuffle=True,random_state=42)
accuracy = []
for tr_idx,ts_idx in kf.split(df_encoded):
    X_train,X_test = df_encoded.iloc[tr_idx],df_encoded.iloc[ts_idx]
    Y_train,Y_test = y.iloc[tr_idx],y.iloc[ts_idx]
    
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)
    svm.fit(X_train,Y_train)
    Y_pred = svm.predict(X_test)
    
    acc= accuracy_score(Y_pred,Y_test)
    accuracy.append(acc)

print(f"Accuracy Score: {accuracy_score(Y_pred,Y_test)}")
print(f"Recall Score: {recall_score(Y_pred,Y_test,average="macro")}")
print(f"Precision Score: {precision_score(Y_pred,Y_test,average="macro")}")
# New unseen data
new_data = {
    "word_freq_free": [0.05],
    "word_freq_win": [0.01],
    "word_freq_offer": [0.00],
    "email_length": [120],
    "num_hyperlinks": [1],
    "sender_domain": ["newdomain@unseen.com"]
}

new_df = pd.DataFrame(new_data)

new_df_encoded = new_df.drop(columns=["sender_domain"])

for col in df_encoded.columns:
    if col not in new_df_encoded.columns:
        new_df_encoded[col] = 0 

# Reorder the columns to match the training data column order
new_df_encoded = new_df_encoded[df_encoded.columns]

# Preprocess the new data (standardize using the saved scaler)
new_df_scaled = scalar.transform(new_df_encoded)  

prediction = svm.predict(new_df_scaled)
print(f"Prediction for unseen email: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
