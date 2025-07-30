import pandas as pd 
from sklearn.linear_model import LinearRegression
import warnings
import pickle
warnings.filterwarnings("ignore")
df=pd.read_excel(r"C:\Users\adars\Downloads\Multi_Data.xlsx")
x=df[["area","bedrooms","age"]]
y=df.price
m1=LinearRegression()
m1.fit(x,y) 
predict=m1.predict([[12000,5,6]])
print("Predicted Price: ₹",predict[0])
with open("areabedage.pkl", "wb") as f:
 pickle.dump(m1, f)
