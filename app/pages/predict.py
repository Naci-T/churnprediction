import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import xgboost as xgb
#import numpy as np 


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-background-with-hexagonal-line-pattern-design_1017-28442.jpg?w=826&t=st=1677494980~exp=1677495580~hmac=2214c1492d75747aaf7f3a1a119c7aedba880f800dd10c11b9b2d2f9f1b03457");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title("Please enter the details to see if the customer will churn or not")

# User input
total_trans_ct = st.number_input('Total transaction count', min_value=0, max_value=200)

total_trans_amt = st.number_input('Total transaction amount', min_value=0, max_value=30000) # 20 = High probability to churn, 80 = Low probability to churn

total_revolving_bal=st.number_input('Total revolving balance', min_value=0, max_value=4000, key="total_revolving_bal")

tac_Q4_Q1=st.number_input('Total amount change from quarter 4 to quarter 1', min_value=0.0, max_value=4.0, step=0.05)

tcc_Q4_Q1= st.number_input('Change in transaction count from quarter 4 to quarter 1', min_value=0.0, max_value=4.0, step=0.05)

trc= st.select_slider('Number of products at the bank', [1,2,3,4,5,6], key="trc")

months_inactive= st.select_slider("Months of inactivity in previous year", [0,1,2,3,4,5,6], key="months_inactive")

contacts_count= st.select_slider("How many times contacted in previous year", [0,1,2,3,4,5,6], key="contacts_count")

age= st.slider("Customer's age", 18,100, key="age")

credit=st.slider("Credit limit", 1000, 40000, key="credit")

mob= st.slider("Months on book", 12, 60, key="mob")

# Loading the model
model_xgb = xgb.XGBClassifier()
model_xgb.load_model("./model/xgbmodel.bin")

# Make prediction: 
user_input = pd.DataFrame([[total_trans_ct, total_trans_amt, total_revolving_bal, tac_Q4_Q1, tcc_Q4_Q1, trc, months_inactive, contacts_count, age, credit, mob]], columns=["Total_Trans_Ct","Total_Trans_Amt", "Total_Revolving_Bal", "Total_Amt_Chng_Q4_Q1", "Total_Ct_Chng_Q4_Q1", "Total_Relationship_Count", "Months_Inactive_12_mon", "Contacts_Count_12_mon", "Customer_Age", "Credit_Limit", "Months_on_book"])
prediction = model_xgb.predict_proba(user_input)

if st.button("Predict"):
    churn_prob = round(prediction[0][1] * 100, 2)
    if churn_prob > 50:
        st.error(f"This customer has a {churn_prob}% chance to churn.")
    else:
        st.success(f"This customer has a {churn_prob}% chance to churn.")