# E-Commerce-Shipping
## Problem Statement 🤩
The e-commerce platform is facing challenges in predicting customer ratings accurately, which can lead to reduced customer satisfaction, lower sales, and negative brand reputation. Despite the availability of customer rating data, the current system lacks the ability to analyze and interpret the data in a meaningful way, resulting in inaccurate predictions. This creates a need for a more sophisticated and accurate machine learning model that can analyze customer rating data to predict customer ratings with high accuracy, leading to improved customer satisfaction, increased sales, and positive brand reputation.

## 📌 Project Overview 🤔 
This project explores an e-commerce dataset (sourced from Kaggle containing electronic product customer data) through a dual-lens approach:
1. **Predictive Modeling (Python):** Building an end-to-end machine learning pipeline to test if supply-chain metadata can forecast customer satisfaction ratings.
2. **Business Intelligence (Excel Dashboard):** Designing a professional, interactive Excel dashboard to track key performance indicators (KPIs) and visualize customer fulfillment trends.

## Dataset Source 📅
The dataset was obtained from the <a href ="https://www.kaggle.com/datasets/prachi13/customer-analytics">E-Commerce Shipping Data</a> from Kaggle. 

## Techniques Used 🕵️‍♀️
* **Languages & Tools:** Python, Microsoft Excel
* **Python Machine Learning Libraries:** Scikit-Learn (`LogisticRegression`, `RandomForestClassifier`, `KNeighborsClassifier`, `CategoricalNB`), Imbalanced-Learn (`SMOTE`, `imblearn.pipeline.Pipeline`)
* **Model Validation & Tuning:** `StratifiedKFold`, `RandomizedSearchCV`, multi-metric tracking (`recall_macro`, `f1_macro`, `accuracy`, `roc_auc`)
* **Excel Data Visualization & BI:** Pivot Tables, Pivot Charts (Pie, Area, Doughnut, Column, Bar charts), Slicers, Camera Tool, and custom color palettes ("Trees During Fall" theme).
  
## Result 🔎
## 🔍 Part 1: Python Machine Learning Pipeline

### Methodology & Experimental Workflow
* **Preprocessing & Leakage Prevention:** Built modular pipelines using Scikit-Learn's `ColumnTransformer` to handle scaling and encoding strictly inside training folds.
* **Class Imbalance Management:** Implemented **SMOTE** via `imblearn` pipelines and benchmarked against models with `class_weight='balanced'`.
* **Hyperparameter Optimization:** Deployed `RandomizedSearchCV` across a 5-Fold Stratified Cross-Validation framework, optimizing for macro-averaged metrics.

### Findings & Insights
* **The Performance Ceiling:** All models (Random Forest, Logistic Regression, KNN, Naive Bayes) consistently capped at **~50% Macro Recall and ROC-AUC** (random-guessing level). 
* **Feature Limitation:** Rigorous validation proved that physical logistics attributes (`weight_in_gms`, `cost_of_the_product`, `warehouse_block`, `mode_of_shipment`) share overlapping distributions and lack direct mathematical correlation with human customer satisfaction ratings.
* **Strategic Takeaway:** Customer sentiment relies on unmeasured qualitative factors (product quality, customer support, item damage) rather than supply-chain metadata alone.
For full explanation, please visit my Medium article, <a href="https://jadangpooiling.medium.com/crisp-dm-methodology-with-python-model-deployment-using-flask-included-classification-case-33b9e184f4e7">CRISP-DM Methodology With Python | Classification Case Study</a>.
---

## 📊 Part 2: Excel Interactive Dashboard & BI Case Study

To complement the predictive modeling limitation, an interactive business intelligence dashboard was built in Microsoft Excel to monitor operations and customer feedback visually.

### Dashboard Architecture & Workflow
* **Data Preparation:** Cleaned and transformed raw data (e.g., standardizing fulfillment flags like converting `0/1` to `OnTime/Late`).
* **Summary & Analysis Engines:** Built **15 pivot tables** across dedicated worksheets to aggregate counts, percentages, and averages for variables like customer care calls, prior purchases, product importance, and discounts.
* **Advanced Visualization & Interactivity:** 
  * Assembled scorecards, icon integration, and structured frameworks using custom color palettes.
  * Implemented Excel's **Camera Tool** to dynamically snapshot summary tables onto the dashboard layout.
  * Added **Slicers** for real-time interactive data filtering across all charts.

Read the full written walkthrough of the dashboard build here: [Build Excel Dashboard for E-Commerce Data](https://medium.com/@jadangpooiling/build-excel-dashboard-for-e-commerce-data-4898d540c6fe).

## Recommendation 📥
* To effectively predict customer dissatisfaction or 1-star reviews in future iterations, the business must collect and integrate qualitative data streams—such as customer service interaction logs, product quality metrics, packaging feedback, or customer sentiment text data—rather than relying solely on supply-chain metadata.
* You may try to build multiclass classification model using this dataset, which means you may not need to map the rating 2 to 5 as 0 before you train the model. For a multiclass multiclass classification model, it will return the result that indicates whether a customer will give rating 1, 2, 3, 4, or 5 specifically, instead of indicating whether a customer will give rating 1 or not.  
