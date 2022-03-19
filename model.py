import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.tree import DecisionTreeClassifier as DT
import pickle

ecomm = pd.read_csv("https://raw.githubusercontent.com/jadanpl/E-Commerce-Shipping/main/ecomm.csv")

# data preprocessing for modeling
dummy1 = pd.DataFrame(pd.get_dummies(ecomm[['Warehouse_block', 'Mode_of_Shipment','Product_importance','Gender']]))
dummy2 = pd.DataFrame(pd.get_dummies(ecomm[['Customer_care_calls','Customer_rating','Prior_purchases']].astype(str)))
ecomm1 = pd.DataFrame(scale(ecomm[['Cost_of_the_Product','Discount_offered', 'Weight_in_gms']]),
                      columns=['Cost_of_the_Product','Discount_offered', 'Weight_in_gms'])
ecomm2 = pd.concat([ecomm1,dummy1,dummy2,ecomm[['Reached.on.Time_Y.N']]],axis=1)

# split data into output and input
X = ecomm2.iloc[:,:-1] # inputs
Y = ecomm2['Reached.on.Time_Y.N'] # outputs

# split data into train data and test data
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25,shuffle=True)

# Decision Tree
DT_model = DT(criterion = 'entropy',max_depth=4)

# Fit the model on dataset
# DT_model.fit(X_train, Y_train)
DT_model.fit(X, Y)

# save the model
filename = 'finalized_dt_model_ecomm.pkl'
pickle.dump(DT_model, open(filename, 'wb'))