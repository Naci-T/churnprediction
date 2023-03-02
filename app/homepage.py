import streamlit as st

def Homepage():
    st.markdown("# Churn Halt ")
    st.sidebar.markdown("# Churn Halt")

def Predict():
    st.markdown("# Churn prediction ")
    st.sidebar.markdown("# Churn prediction ")

def Tableau():
    st.markdown("# Tableau ")
    st.sidebar.markdown("# Tableau ")

page_names_to_funcs = {
    "Main Page": Homepage,
    "Page 2": Predict,
    "Page 3": Tableau,
}

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-color-background-gradient-abstract-modern_343694-2130.jpg?w=826&t=st=1677495167~exp=1677495767~hmac=8695c6bbf17e5b28ac9aa25b002e83829f37f83326cf9e7b3a1184b76a44e46a");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title("Welcome to Churn Halt!")

st.write("This website is designed to help banks predict which customers are likely to churn, and provide valuable insights on how to retain them. With Churn Halt, you can access our powerful machine learning models to analyze customer behavior and other key factors to determine the likelihood of churn.")
st.write("Our user-friendly interface makes it easy for you to make predictions with just a few clicks, and our advanced algorithms will provide you with accurate insights and recommendations on how to keep your customers engaged and satisfied. With Churn Halt, you can reduce customer churn, improve customer loyalty, and ultimately increase your revenue.")
st.write("In addition, we've created a separate page where you can visualize the data using Tableau Public. Here, you can explore the patterns and trends in customer behavior and gain deeper insights into the factors that drive customer churn.")
st.write("So, whether you're a small credit union or a large multinational bank, Churn Halt can help you take control of your customer retention strategy and improve your bottom line. Let's get started!")
# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()