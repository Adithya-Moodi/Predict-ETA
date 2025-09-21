# Predict-ETA

Predicting Delivery ETA for E-commerce Orders
----------------------------------------------
This project focuses on predicting the Estimated Time of Arrival (ETA) for e-commerce deliveries using Machine Learning.
The solution leverages XGBoost Regressor with Optuna hyperparameter tuning to achieve accurate predictions and includes a Streamlit UI for real-time interaction.


Project Overview
---------------------------------------------
Developed an XGBoost regression model to predict delivery ETA.
Applied Optuna for efficient hyperparameter optimization.
Conducted residual analysis and stress testing to ensure robustness under edge cases (long distances, unusual, locations).
Achieved strong predictive performance with:
R² Score: XX.XX
MSE: YY.YY
Built a Streamlit web application for uploading order data, generating predictions, and visualizing results.


Tech Stack
---------------------------------------------
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Optuna, Matplotlib, Seaborn
UI: Streamlit


How to Run the Project
---------------------------------------------
Clone the repository:
git clone https://github.com/Adithya-Moodi/Predict-ETA


Install dependencies:
---------------------------------------------
https://github.com/Adithya-Moodi/Predict-ETA
pip install -r requirements.txt


Run the Streamlit app:
---------------------------------------------
streamlit run app.py


Model Performance
---------------------------------------------
R² Score: 0.9804
RMSE: 2.6841


The model was validated using cross-validation, residual analysis, and stress testing for robustness.
---------------------------------------------
Streamlit App Features


Future Improvements
---------------------------------------------
Incorporate live traffic and weather data
Experiment with deep learning models (e.g., LSTM for time-series ETA prediction)
Containerize app using Docker for scalable deployment

Author
---------------------------------------------
Adithya Moodi

