# Medical_insurance_charges_prediction
Predicting sales of unique products which belongs to different stores with their weight and establishment year through connecting SQL Server Database and Power Bi Dashboard and deploy it on AWS.

# Input values:
![](https://github.com/naveen12334/Medical_insurance_charges_prediction/blob/main/Images/Input_values.PNG)

# Result:
![](https://github.com/naveen12334/Medical_insurance_charges_prediction/blob/main/Images/Prediction.PNG)

# PROBLEM STATEMENT:
The goal of this project is to allows a person to get an idea about the necessary amount required according to their own health status. Later they can comply with any health insurance company and their schemes & benefits keeping in mind the predicted amount from our project. This can help a person in focusing more on the health aspect of an insurance rather than the futile part

# Goal:
the goal is to predict the insurance charges of the Customers of Healthcare Service according to the provided dataset based on the age,gender,bmi etc.

# Approach:
The classical machine learning tasks like Data Exploration, Data Cleaning,Feature Engineering, Model Building and Model Testing. Try out different machine learning algorithms that’s best fit for the above case.

# Project Various Steps:

# Data Source (SQL VM):
![](https://github.com/naveen12334/Medical_insurance_charges_prediction/blob/main/Images/SQL_charges.PNG)

# Data Transformation and Extraction:
Data is transformed into SQL Server from csv files and extract in python notebook from SQL Server through making a connection with pyodbc library.

# Data Exploration:
I started exploring datasets using pandas, NumPy,matplotlib and seaborn.

# Model Selection:
Made many Models But selected RandomForest Regressor.

# Hyperparameter Optimization:
Using Randomizedsearch CV to select the best parameter for training the model

# Model Dump:
As per selected trained model is dumped to pickled format for app development

# Model Accuracy 
# Training : 90%
# Testing  : 88%

# Export data with predicted result back to SQL Server:
![](https://github.com/naveen12334/Medical_insurance_charges_prediction/blob/main/Images/SQL_Predicted_Charges.PNG)

# PowerBI Report:
![](https://github.com/naveen12334/Medical_insurance_charges_prediction/blob/main/Images/Power%20Bi%20Report.PNG)

# Deployed:
Deployed on AWS -- http://medicalinsurancepred-env.eba-mgukfuav.us-west-2.elasticbeanstalk.com/









