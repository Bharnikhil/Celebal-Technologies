# 🏡 House Prices - Linear Regression with Data Preprocessing and Feature Engineering

This project is a solution to the [Kaggle House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) competition. The goal is to predict housing sale prices using regression techniques after thorough data preprocessing and feature engineering.

---

## 📁 Files Included

| File Name                           | Description |
|------------------------------------|-------------|
| `train.csv`                        | Training dataset containing features and `SalePrice` (target) |
| `test.csv`                         | Test dataset without the target variable |
| `House_Prices_Linear_Regression.ipynb` | Jupyter notebook with all code: preprocessing, feature engineering, model training, and predictions |
| `submission.csv`                   | Submission file generated using predictions on the test set |
| `README.md`                        | This file – explains the workflow and contents |

---

## 🎯 Objective

To build a **Linear Regression model** that can accurately predict `SalePrice` of houses based on over 70 input features.

---

## 🔍 Workflow Summary

### 1. Data Loading
- Merged `train.csv` and `test.csv` for uniform preprocessing
- Extracted `SalePrice` and `Id` columns

### 2. Handling Missing Values
- Imputed:
  - Categorical features like `PoolQC`, `Alley`, `FireplaceQu` with `'None'`
  - Numerical features like `GarageArea`, `BsmtFinSF1` with `0`
  - Mode imputation for features like `KitchenQual`, `SaleType`
  - Median imputation of `LotFrontage` based on `Neighborhood`

### 3. Feature Engineering
- Created new features like:
  - `HouseAge`, `RemodAge`, `GarageAge`
  - `TotalSF`, `TotalBath`, `TotalPorchSF`
  - Flags: `HasPool`, `HasGarage`, `HasFireplace`, `HasPorch`

### 4. Encoding
- Label Encoding for ordinal features (e.g., `ExterQual`, `BsmtQual`)
- One-hot encoding for nominal categorical variables

### 5. Model Building
- Used `LinearRegression` from `sklearn`
- Trained on 80% of the data and validated on 20%
- Evaluated using **RMSE** (Root Mean Squared Error)

### 6. Submission
- Trained the model on full dataset
- Predicted `SalePrice` for `test.csv`
- Generated `submission.csv` in the required format

---

## 🧠 Key Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`: for modeling and preprocessing

---

## 📦 Future Improvements

- Try regularized models: `Ridge`, `Lasso`, `ElasticNet`
- Log-transform `SalePrice` for better residual distribution
- Feature selection using permutation importance

---

## 🏁 Output Sample

| Id    | SalePrice |
|-------|-----------|
| 1461  | 125000.0  |
| 1462  | 154000.0  |
| 1463  | 134500.0  |
| ...   | ...       |

---

## ✅ How to Use

1. Clone/download the repo
2. Open the Jupyter notebook: `House_Prices_Linear_Regression.ipynb`
3. Run all cells or run step-by-step to explore
4. Upload `submission.csv` to Kaggle to evaluate performance

---

## 📌 License
This project is for educational and competition purposes on Kaggle.
