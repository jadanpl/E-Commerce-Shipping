import pandas as pd
from sklearn.preprocessing import scale
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load dataset
ecomm = pd.read_csv("https://raw.githubusercontent.com/jadanpl/E-Commerce-Shipping/main/E-Commerce%20Shipping%20Data.csv")

# Rename columns
cols=[]
for i in ecomm.columns[1:-1]:
    i = i.lower()
    cols.append(i);
cols = ['ID'] +  cols
cols.append('arrival')
ecomm.columns = cols

# Data preprocessing
ecomm['gender'] = ecomm.gender.map({'F':0, 'M':1})
ecomm['customer_rating'] = ecomm['customer_rating'].map({5:0, 4:0, 3:0, 2:0, 1:1})
dummy = pd.DataFrame(pd.get_dummies(ecomm[['warehouse_block', 'mode_of_shipment','product_importance']]))
ecomm1 = pd.DataFrame(scale(ecomm[['cost_of_the_product','weight_in_gms','discount_offered']]),
                      columns=['cost_of_the_product','weight_in_gms','discount_offered'])
ecomm_final = pd.concat([ecomm1,dummy,ecomm[['customer_care_calls', 'prior_purchases','gender', 'arrival','customer_rating']]],
                        axis=1)

# Split data into output and input
X = ecomm_final.iloc[:,:-1] # inputs
Y = ecomm_final['customer_rating'] # outputs

# Model building
KNN_model = KNeighborsClassifier(n_neighbors=11, metric='euclidean')
KNN_model.fit(X, Y)

# Save the model
filename = 'finalized_knn.pkl'
pickle.dump(KNN_model, open(filename, 'wb'))
