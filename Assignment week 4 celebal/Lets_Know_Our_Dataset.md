📁 Let's Know Our Dataset
This folder contains the datasets and solution for Week 4 Assignment, focused on performing Exploratory Data Analysis (EDA) using the Titanic Survival Dataset.

🎯 Objective
The purpose of this assignment is to perform in-depth EDA to:
Understand the structure and meaning of the data.
Identify patterns, missing values, and outliers.
Discover relationships between features and survival outcomes.
Support findings with appropriate visualizations.

📂 Files in This Folder
| File Name                  | Description                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `train.csv`                | **Main training dataset**. Includes passenger information and whether they survived (`Survived` = 0/1). Used for EDA and model training. |
| `test.csv`                 | Same structure as `train.csv` but without the `Survived` column. Used for testing the model.                                             |
| `gender_submission.csv`    | A sample submission showing expected format (PassengerId + Survived) for submitting predictions on Kaggle.                               |
| `Titanic_EDA.ipynb`        | Jupyter Notebook containing the complete EDA: analysis, visualizations, and insights derived from the training dataset.                  |
| `Lets_Know_Our_Dataset.md` | This file! It explains the context and helps others understand the datasets and your analysis approach.                                  |

🧾 Dataset Summary
The Titanic dataset is one of the most popular datasets used for binary classification problems.
Key features in the dataset:
| Column Name   | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `PassengerId` | Unique ID for each passenger                                         |
| `Survived`    | 0 = Did not survive, 1 = Survived                                    |
| `Pclass`      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)                             |
| `Name`        | Full name of the passenger                                           |
| `Sex`         | Gender                                                               |
| `Age`         | Age in years                                                         |
| `SibSp`       | # of siblings/spouses aboard                                         |
| `Parch`       | # of parents/children aboard                                         |
| `Ticket`      | Ticket number                                                        |
| `Fare`        | Passenger fare                                                       |
| `Cabin`       | Cabin number (many missing values)                                   |
| `Embarked`    | Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

🔍 What You'll Find in the Notebook
The notebook performs the following:
Missing value analysis with heatmaps and imputation suggestions.
Distribution plots for age and fare.
Survival analysis based on class, sex, and embarkation.
Outlier detection using boxplots.
Correlation matrix with heatmaps.
Feature engineering (like family size).
Summary of insights from the EDA.

📌 Conclusion
This analysis helps build a strong foundation for modeling survival prediction using machine learning. The EDA also demonstrates how real-world datasets often require cleaning, exploration, and visualization before modeling.


