# Customer Churn Prediction App Readme
This is a Streamlit app (https://naci-t-churnprediction-apphomepage-x6x5ug.streamlit.app/) for predicting customer churn using an XGBoost binary classification model. The user interface provides sliders and number input boxes for the user to input information such as total transaction count, total transaction amount, total revolving balance, etc. After the user has entered the information and clicks on the "Predict" button, the app displays the probability of the customer churning.

# How to Use
To use the app, simply run the script and access it through a web browser. The app will display a title and various input fields for the user to fill in. The user can input information such as the total transaction count, total transaction amount, total revolving balance, and more. After entering the required information, the user can click on the "Predict" button to obtain the probability of customer churn.

# Model Used
The model used in this app is an XGBoost classifier. It has been pre-trained and loaded from a saved model file. The model takes the user input as a Pandas DataFrame and uses the predict_proba() method to predict the probability of customer churn. 

# Improvements
This app can be further improved by adding more features, allowing for user feedback, and displaying additional information about the model's performance. Additionally, it can be useful to provide explanations for the user as to why certain inputs are required and what they mean.