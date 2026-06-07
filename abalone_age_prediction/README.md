# Classical Machine Learning Course Project

## Team
**Members:**
- Evgeniya Yankovich
- Katsiaryna Schastnaya

---

## Project Title
Abalone Age Prediction Using Supervised Regression

---

## Objective
The goal of this project is to predict the age of abalone based on physical measurements.  
Age is estimated using the number of rings, which is a standard proxy in biological studies.

The task is formulated as a **supervised regression problem**.

---

## Dataset
**Source:** UCI Machine Learning Repository – Abalone Dataset  
The dataset contains physical characteristics of abalone specimens, including size, weight, and sex.

---

## Project Stages

1. Exploratory Data Analysis & Preprocessing
2. Feature Engineering & Feature Selection
3. Baseline and Advanced Models
4. Model Selection & Hyperparameter Optimization
5. Evaluation & Error Analysis
6. Explainability
7. Demo Application

---

## How to Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit demo application:

```
streamlit run app.py
```

The application will open in a web browser at http://localhost:8501.

---

## Results

**Baseline model (Linear Regression):** evaluated using cross-validated MAE ≈ 1.55 

**Final model (Gradient Boosting Regressor):**

- Achieved the lowest cross-validated MAE ≈ 1.51 

- Demonstrated stable performance across folds

- Showed good generalization on the test set

- Error analysis indicates strong performance in the central age range, with increased errors for extreme values due to data sparsity.

---
## Conclusions

Feature engineering and careful model selection significantly improved predictive performance compared to the baseline.
Explainability analysis confirms that the model relies primarily on physically meaningful size and weight features, which aligns with domain knowledge.

The Streamlit application provides a convenient way to test the model on new inputs and demonstrate its behavior interactively.

---
## Limitations
- Limited number of samples for very old abalones

- Predictions are based solely on physical measurements

- Performance may degrade when extrapolating to extreme case

---
## Notes
This project was developed as part of a classical machine learning coursework and is intended for educational and demonstration purposes.