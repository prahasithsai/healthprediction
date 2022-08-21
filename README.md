# mentalhealthprediction
Project Details: 
* Client: Innodatatics
* Project Title:  “Mental Health Wellbeing Analysis of young children during at Pandemic Times”
* Scope of the Project: During the covid pandemic, during lock downtime kids are taking online classes. We have to study the survey and perform various machine learning techniques and come up with the best model that studies the children wellbeing by performing clustering and also finding out those factors that are important for children wellbeing. 
* Project Management Methodology used: CRISP-ML(Q)
***********************************************************************************************************************************************************************
* Stage – 1:
* 1a) Business Understanding:
•	Business Objective: To identify the factors which affect the mental health conditions of child during covid19 & to determine whether the child is suffering from any difficulties. (expected/ border line/ clinically significant).
•	Business Constraint: To select the top most relevant features for solving the business problem & to handle the imbalance data.
* 1b) Data Understanding:
•	Data Collection: Primary Data Source - The raw data collected around ‘59’ features of the child through a survey from the primary school children when they were in the lock down which was provided by the client. 
* 1c) Data Types: It has 1) Continuos measure – Interval data 2) Discrete measure – a) categorical – Nominal & Ordinal data b) binary data & c) count data.
***********************************************************************************************************************************************************************
* Stage – 2:
* 2a) Data Preprocessing/wrangling: It includes:
* Labelling the categorical features – Performed one hot encoding, mapping the classes to its given subscores & calculating the total scores for  output feature as per the instructions given in the dataset.
* Topic Modelling on textual features – For handling textual data, filtered the stop words,special characters,digits & finally used the strip function to extract the required strings.
* Handling the missing values – As missing values are found it is addressed by using imputation.
* Discretization/Binning/Grouping – Based upon the total scores of ouput feature those are binned & labelled into (expected/ border line/ clinically significant) difficulties.
* 2b) Feature Engineering: 
Created a new feature – “sleeping hours” based on the features of sleeping time & waking time of the child.
* 2c) Feature Selection: Used KBest method with score function - Chi-squared stats of non-negative features for classification tasks for selcting top best features.
* 2d) Exploratory Data Analysis(EDA): Used heat map for visualizing the correlation coefficient between input features & dropped those features which are exceeding the thresh hold limit of r >= 0.80
*********************************************************************************************************************************************************************** 
* Stage – 3:
* 3) Data Mining/Machine Learning/Model Building & its Evaluation:
* Handling the target feature – As the output classes are imbalanced used stratified K fold technique before proceeding into model building.
* Data Partition – Entire data is partitioned into a) train data (60%) b) Validation data (20%) & c) test data (20%)
* Model Building – Performed using ‘3’ models:
* a)	Using Logistic Regression with stratified K Fold:
Parameters like ‘one vs rest’, newton solver – effective in large datasets
* b)	Using XGBoosting with stratified K Fold:
Estimator – Decision Tree, hyper parameter tuning using Randomized search CV using parameters max_depth, learning_rate.
* c)	Using Random Forest Classifier with stratified K Fold:
Estimator uesd – Decision Tree, other parameters like max_depth.
•	Evaluation Metrics  used – f1 score, confusion matrix:
F1 scores : 'Logistic Regression' : 0.91, 'XG boost' : 0.90, 'RandomForest' : 0.91
•	Among them Random Forest Classifier has best performance & created a model file & saving into pickle format.
***********************************************************************************************************************************************************************
* Stage – 4:
4) Model Deployment & Monitoring & Manitenance:
* On local environment – Using Flask API, model pickle file, html for user interface.
***********************************************************************************************************************************************************************
* Note:
* Please refer 'model.py' for the code file & documentation file in 'Project Documentation' file
* Attachments:
•	Link: https://github.com/prahasithsai/healthprediction
•	Deployment Link: https://mentalhealthprediction.herokuapp.com/

