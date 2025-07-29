import pandas as pd 
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import warnings
import pickle
warnings.filterwarnings("ignore")
df=pd.read_excel(r"C:\Users\adars\Downloads\Multi_Data.xlsx")
# print(df)
x=df[["area","bedrooms","age"]]
y=df.price
# print(x)
# print(y)
m1=LinearRegression()
m1.fit(x,y) 
predict=m1.predict([[12000,5,6]])
print("Predicted Price: ₹",predict[0])
with open("areabedage.pkl", "wb") as f:
 pickle.dump(m1, f)