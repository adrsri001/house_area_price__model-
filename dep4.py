import pickle
import streamlit as st
m1=pickle.load(open("areabedage.pkl","rb"))

def mydeploy():
    st.title("Area price Predication")
    st.subheader("[Acorrding to Bedroom and How many years old is the house]")
    area=st.number_input("Enter your area: ")
    bedroom=st.number_input("Enter number of Bedrooms: ")
    age=st.number_input("How many years old is the house?: ")
    pred=st.button("Predicat")
    if pred :
        x=m1.predict([[area,bedroom,age]])
        st.write("Price of area is Rs",x[0])
mydeploy() 