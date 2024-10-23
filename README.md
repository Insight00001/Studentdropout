# Table of Contents
* Data Cleaning
* Exploratory Data Analysis
        Univariate Analysis
        Bivariate Analysis
        Multivariate Analysis
* Model Development
* Model Evaluation
* Hyper-parameter Tuning
* Model Deployment
* How to Run the Project
* Results
# Data Cleaning
* Missing values: Handled using statistical imputation (mean/median for numerical and mode for categorical data).
* Duplicate values: No duplicates were found.
* Outliers: Detected using Z-score and boxplots, with appropriate handling applied.
* Standardization: Numerical features were standardized using Z-score normalization.
* Encoding: Categorical features were encoded using LabelEncoder and One-Hot Encoding.
# Exploratory Data Analysis
## Univariate Analysis
    * Numerical Features: Analyzed and visualized using histograms.
    * Categorical Features: Visualized using count plots.
## Bivariate Analysis
    * Numerical: Correlation matrix and scatter plots were used.
    * Categorical: Boxplots and heatmaps were utilized to display relationships.
## Multivariate Analysis
    * Pair plots: Used to explore the relationships between multiple variables.
# Model Development
The following models were developed and compared:

    * Logistic Regression
    * Decision Tree Classifier
    * Random Forest Classifier
    * Support Vector Machine (SVM)
    * XGBoost
    * Convolutional Neural Network (CNN) using TensorFlow
# Performance Metrics:
    * Accuracy
    * Precision
    * Recall
    * F1-score
    * ROC-AUC
# Model Evaluation
    Performance of models was evaluated using the metrics above.
    Cross-validation using K-folds was employed to prevent overfitting.
# Hyper-parameter Tuning
Several hyper-parameter optimization techniques were employed:

    * Grid Search
    * Randomized Search
    * Bayesian Optimization
Each of these methods was applied to the Logistic Regression, Decision Tree, RandomForest, support vector machine, XGBoost models.

# Model Deployment
The best-performing model was deployed using Streamlit. You can access the deployed application here: [Streamlit App](https://predictionappl.streamlit.app/).

The code and project files are available in this repository for review and further usage.
