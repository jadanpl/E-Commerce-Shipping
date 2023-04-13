# E-Commerce-Shipping
For full explanation, please read my Medium article, <a href="https://jadangpooiling.medium.com/crisp-dm-methodology-with-python-model-deployment-using-flask-included-classification-case-33b9e184f4e7">CRISP-DM Methodology With Python (Model Deployment Using Flask Included) | Classification Case Study Using KNN Model</a>.

## Problem Statement 🤩
The e-commerce platform is facing challenges in predicting customer ratings accurately, which can lead to reduced customer satisfaction, lower sales, and negative brand reputation. Despite the availability of customer rating data, the current system lacks the ability to analyze and interpret the data in a meaningful way, resulting in inaccurate predictions. This creates a need for a more sophisticated and accurate machine learning model that can analyze customer rating data to predict customer ratings with high accuracy, leading to improved customer satisfaction, increased sales, and positive brand reputation.

## Objective 🤔
To achieve an accuracy rate of at least 80% in predicting customer ratings within a year using specific order details. This will help businesses make data-driven decisions about their products, marketing strategies, and customer service.

## Dataset Source 📅
The dataset was obtained from the <a href ="https://www.kaggle.com/datasets/prachi13/customer-analytics">E-Commerce Shipping Data</a> from Kaggle. 

## Techniques Used 🕵️‍♀️
To determine whether a customer would give rating 1, we can map the rating 2 to 5 as 0 to represent rating other than 1. It will become a <b>binary classification</b>  instead of a multiclass classification. 

## Result 🔎
The final model is a k-Nearest Neighbors (KNN) classifier. The final model returned accuracy score of about 77.60% for the testing data. Besides, I also created a flask application with a proper frontend and UI that can be run on the local computer (as shown in the video below).


https://user-images.githubusercontent.com/57357735/230870228-6b66ab5c-1b04-485e-86e8-bd7b81fd34eb.mp4


## Recommendation 📥
* Use other classification machine learning algorithms, such as support vector machine, random forest classifier, and logistic regression. 
* Utilize Randomized Search or Grid Search to tune the hyperparameters to check if the accuracy score would be higher.
* Handle the class imbalance using SMOTE, SMOTE-TOMEK, ADASYN, or SMOTE-ENN techniques.  
* You may try to build multiclass classification model using this dataset, which means you may not need to map the rating 2 to 5 as 0 before you train the model. For a multiclass multiclass classification model, it will return the result that indicates whether a customer will give rating 1, 2, 3, 4, or 5 specifically, instead of indicating whether a customer will give rating 1 or not.  
