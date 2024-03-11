import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv("C:\\Users\\Dell\\Downloads\\water_potability.csv")
df.head()
df["ph"] = df["ph"].fillna(df["ph"].mean())
df["Sulfate"] = df["Sulfate"].fillna(df["Sulfate"].mean())
df["Trihalomethanes"] = df["Trihalomethanes"].fillna(df["Trihalomethanes"].mean())
x = df.drop(["Potability","Chloramines","Sulfate","Organic_carbon","Trihalomethanes"],axis=1)
y = df["Potability"]
scaler = StandardScaler()
x = scaler.fit_transform(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


#Creating object of Model
model_svm = SVC(kernel="rbf")
#Model training
model_svm.fit(x_train,y_train)
#Make prediction
pred_svm = model_svm.predict(x_test)
accuracy_score_svm = accuracy_score(y_test,pred_svm)
print(accuracy_score_svm*100)