# NYC Airbnb Price Prediction

Individual ML project. Topic assigned by course instructor.

## Objective

Predict the nightly price of Airbnb listings in New York City based on listing characteristics: location, room type, host activity, and review metrics.

**Task type:** Supervised regression

**Dataset:** [AB_NYC_2019](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) — ~49,000 Airbnb listings in NYC with price as the target variable.

---

## What was done

**EDA** — distribution of prices (right-skewed, median $106 vs mean $153), missing value analysis, relationships between price and room type / borough / location. Geographic price distribution visualized on a NYC borough map.

**Preprocessing** — dropped irrelevant columns (`name`, `host_name`, `last_review`), filled missing `reviews_per_month` with 0, applied One-Hot Encoding to categorical features (`room_type`, `neighbourhood_group`, `neighbourhood`), applied log1p transformation to the target variable to reduce sensitivity to outliers, 80/20 train-test split.

**Models trained and compared:**
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

**Evaluation metrics:** MAE, RMSE, R² (on log-transformed target).

**Result:** Random Forest achieved the best performance. Decision Tree showed signs of overfitting. Linear Regression confirmed that pricing is not purely linear.

---

## Files

- `Small_Project_Evgeniya_Y.ipynb` — full analysis and modeling notebook
- `New_York_City_.png` — NYC borough map used for geographic visualization

>Note:
This project was developed as part of a classical machine learning coursework and is intended for educational and demonstration purposes.
