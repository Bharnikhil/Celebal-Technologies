# Machine Learning Model Training & Hyperparameter Tuning

This project demonstrates the process of:
- Training multiple Machine Learning models.
- Evaluating models using performance metrics like **Accuracy**, **Precision**, **Recall**, and **F1-Score**.
- Applying **GridSearchCV** and **RandomizedSearchCV** for hyperparameter tuning.
- Selecting the best-performing model based on evaluation metrics.

## 📊 Models Used
- Random Forest Classifier
- Support Vector Machine (SVM)
- Logistic Regression

## ⚙️ Techniques Applied
- **Train-Test Split** for dataset preparation.
- **Model Evaluation Metrics:** 
  - Accuracy
  - Precision (macro-average)
  - Recall (macro-average)
  - F1-Score (macro-average)
- **Hyperparameter Tuning:** 
  - `GridSearchCV` for Random Forest
  - `RandomizedSearchCV` for SVM

## 📈 Results
- Initial model performance compared across metrics.
- Tuned models evaluated for improved performance.

## 🗂 Dataset
The example uses the **Iris dataset** from `sklearn.datasets`. You can replace it with any custom dataset.

## 🔗 Resources
- [KDnuggets: Hyperparameter Tuning Explained](https://www.kdnuggets.com/hyperparameter-tuning-gridsearchcv-and-randomizedsearchcv-explained)

## 🏁 Getting Started
1. Clone the repository:
git clone <repository-url>
cd <repository-folder>
2. Install dependencies:
pip install scikit-learn pandas numpy
3. Run the script:
python model_training.py

## ✅ Future Improvements
- Add more models like XGBoost, KNN, etc.
- Add visualization of metric comparisons.
- Implement cross-validation evaluation.

## 👨‍💻 Author
Nikhil Bhardwaj
