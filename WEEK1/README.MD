##	Data Preprocessing Report for School Dropout
Educational institutions need accurate predictive models to identify students at risk of dropping out. This project aims to develop and optimize predictive models to forecast student dropout rates and recommend interventions to improve retention and student success.

##	Dataset Overview
Dataset Description: the dataset contains 4424 row and 37 columns
Target variable: the target variable is categorical representing the status of students:
Dropout: students who did not complete their education
Enrolled: students who are still in school
Graduated: students who completed their education

##	Data Quality Check
Missing values: there are no missing values in the dataset
Duplicate values: there are no duplicate values in the dataset
Outliers detection: outliers where detected using boxplot and z-score

##	Feature Engineering
Encoding categorical variables:
Label encoding: this techniques was used to convert categorical variables to numerical, the target output containing Dropout, Enrolled, and Graduated this approach of conversion is suitable for multiclass classification problem
##	Handling imbalanced data
Class weights:  for algorithms such as random forest, and logistic regression, class weight was added to balance assign a higher penalty for misclassifying the minority class i.e. enrolled and dropout.

##	Data Transformation
Scaling of features
Standard scalar: I use this techniques to scale numerical features to mean of zero and standard deviation of 1 to prevent models sensitive to feature scaling to be biased by large values e.g. logistic Regression, support vector machine.
Feature Selection
Filter method
F_Classif Test method: I applied the f_classif method to find features that have high correlation with the target variable, features with low correlation where dropped.
Data Splitting
Train test split: the dataset was split into 80% training and 20% testing
Select Kbest features: I applied Kbest to choose the top ten features that has the highest relevance to the target variable.
Final dataset:
The final dataset has a feature of 10 and rows of 4423



