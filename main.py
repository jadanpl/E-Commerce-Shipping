pip install -r requirements.txt
from flask import Flask, render_template, request
import numpy as np
import pickle

# loading the pickle file
model = pickle.load(open('finalized_dt_model_ecomm.pkl','rb'))

# instantiating an object of Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def submit():
    global Weight_in_gms, Cost_of_the_Product, Discount_offered, Gender_F, Gender_M
    global Warehouse_block_A, Warehouse_block_B, Warehouse_block_C, Warehouse_block_D, Warehouse_block_F
    global Mode_of_Shipment_Flight, Mode_of_Shipment_Road, Mode_of_Shipment_Ship
    global Product_importance_high, Product_importance_low, Product_importance_medium
    global Customer_care_calls_2, Customer_care_calls_3, Customer_care_calls_4, Customer_care_calls_5, Customer_care_calls_6, Customer_care_calls_7
    global Customer_rating_1, Customer_rating_2, Customer_rating_3, Customer_rating_4, Customer_rating_5
    global Prior_purchases_2, Prior_purchases_3, Prior_purchases_4, Prior_purchases_5, Prior_purchases_6, Prior_purchases_7, Prior_purchases_8, Prior_purchases_10

    # HTML to .py
    if request.method == "POST":
        Warehouse_block = request.form["Warehouse_block"]
        if (Warehouse_block == "A"):
            Warehouse_block_A = 1
            Warehouse_block_B = 0
            Warehouse_block_C = 0
            Warehouse_block_D = 0
            Warehouse_block_F = 0
        elif Warehouse_block == "B":
            Warehouse_block_A = 0
            Warehouse_block_B = 1
            Warehouse_block_C = 0
            Warehouse_block_D = 0
            Warehouse_block_F = 0
        elif Warehouse_block == "C":
            Warehouse_block_A = 0
            Warehouse_block_B = 0
            Warehouse_block_C = 1
            Warehouse_block_D = 0
            Warehouse_block_F = 0
        elif Warehouse_block == "D":
            Warehouse_block_A = 0
            Warehouse_block_B = 0
            Warehouse_block_C = 0
            Warehouse_block_D = 1
            Warehouse_block_F = 0
        elif Warehouse_block == "F":
            Warehouse_block_A = 0
            Warehouse_block_B = 0
            Warehouse_block_C = 0
            Warehouse_block_D = 0
            Warehouse_block_F = 1

        Mode_of_Shipment = request.form["Mode_of_Shipment"]
        if Mode_of_Shipment == "Ship":
            Mode_of_Shipment_Flight = 0
            Mode_of_Shipment_Road = 0
            Mode_of_Shipment_Ship = 1
        elif Mode_of_Shipment == "Flight":
            Mode_of_Shipment_Flight = 1
            Mode_of_Shipment_Road = 0
            Mode_of_Shipment_Ship = 0
        elif Mode_of_Shipment == "Road":
            Mode_of_Shipment_Flight = 0
            Mode_of_Shipment_Road = 1
            Mode_of_Shipment_Ship = 0

        Product_importance = request.form["Product_importance"]
        if Product_importance == "low":
            Product_importance_high = 0
            Product_importance_low = 1
            Product_importance_medium = 0
        elif Product_importance == "medium":
            Product_importance_high = 0
            Product_importance_low = 0
            Product_importance_medium = 1
        elif Product_importance == "high":
            Product_importance_high = 1
            Product_importance_low = 0
            Product_importance_medium = 0

        Customer_care_calls = request.form["Customer_care_calls"]
        if Customer_care_calls == "2":
            Customer_care_calls_2 = 1
            Customer_care_calls_3 = 0
            Customer_care_calls_4 = 0
            Customer_care_calls_5 = 0
            Customer_care_calls_6 = 0
            Customer_care_calls_7 = 0
        elif Customer_care_calls == "3":
            Customer_care_calls_2 = 0
            Customer_care_calls_3 = 1
            Customer_care_calls_4 = 0
            Customer_care_calls_5 = 0
            Customer_care_calls_6 = 0
            Customer_care_calls_7 = 0
        elif Customer_care_calls == "4":
            Customer_care_calls_2 = 0
            Customer_care_calls_3 = 0
            Customer_care_calls_4 = 1
            Customer_care_calls_5 = 0
            Customer_care_calls_6 = 0
            Customer_care_calls_7 = 0
        elif Customer_care_calls == "5":
            Customer_care_calls_2 = 0
            Customer_care_calls_3 = 0
            Customer_care_calls_4 = 0
            Customer_care_calls_5 = 1
            Customer_care_calls_6 = 0
            Customer_care_calls_7 = 0
        elif Customer_care_calls == "6":
            Customer_care_calls_2 = 0
            Customer_care_calls_3 = 0
            Customer_care_calls_4 = 0
            Customer_care_calls_5 = 0
            Customer_care_calls_6 = 1
            Customer_care_calls_7 = 0
        elif Customer_care_calls == "7":
            Customer_care_calls_2 = 0
            Customer_care_calls_3 = 0
            Customer_care_calls_4 = 0
            Customer_care_calls_5 = 0
            Customer_care_calls_6 = 0
            Customer_care_calls_7 = 1

        Customer_rating = request.form["Customer_rating"]
        if Customer_rating == "1":
            Customer_rating_1 = 1
            Customer_rating_2 = 0
            Customer_rating_3 = 0
            Customer_rating_4 = 0
            Customer_rating_5 = 0
        elif Customer_rating == "2":
            Customer_rating_1 = 0
            Customer_rating_2 = 1
            Customer_rating_3 = 0
            Customer_rating_4 = 0
            Customer_rating_5 = 0
        elif Customer_rating == "3":
            Customer_rating_1 = 0
            Customer_rating_2 = 0
            Customer_rating_3 = 1
            Customer_rating_4 = 0
            Customer_rating_5 = 0
        elif Customer_rating == "4":
            Customer_rating_1 = 0
            Customer_rating_2 = 0
            Customer_rating_3 = 0
            Customer_rating_4 = 1
            Customer_rating_5 = 0
        elif Customer_rating == "5":
            Customer_rating_1 = 0
            Customer_rating_2 = 0
            Customer_rating_3 = 0
            Customer_rating_4 = 0
            Customer_rating_5 = 1

        Prior_purchases = request.form["Prior_purchases"]
        if Prior_purchases == "2":
            Prior_purchases_2 = 1
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "3":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 1
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "4":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 1
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "5":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 1
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "6":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 1
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "7":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 1
            Prior_purchases_8 = 0
            Prior_purchases_10 = 0
        elif Prior_purchases == "8":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 1
            Prior_purchases_10 = 0
        elif Prior_purchases == "10":
            Prior_purchases_2 = 0
            Prior_purchases_3 = 0
            Prior_purchases_4 = 0
            Prior_purchases_5 = 0
            Prior_purchases_6 = 0
            Prior_purchases_7 = 0
            Prior_purchases_8 = 0
            Prior_purchases_10 = 1

        Gender = request.form["Gender"]
        if Gender == "F":
            Gender_F = 1
            Gender_M = 0
        elif Gender == "M":
            Gender_F = 0
            Gender_M = 1

        Cost_of_the_Product = int(request.form["Cost_of_the_Product"])
        Discount_offered = int(request.form["Discount_offered"])
        Weight_in_gms = int(request.form["Weight_in_gms"])

    # .py to HTML
    # Get prediction results
    x = np.array([Cost_of_the_Product, Discount_offered, Weight_in_gms, Gender_F, Gender_M,
                  Warehouse_block_A, Warehouse_block_B, Warehouse_block_C, Warehouse_block_D, Warehouse_block_F,
                  Mode_of_Shipment_Flight, Mode_of_Shipment_Road, Mode_of_Shipment_Ship,
                  Product_importance_high, Product_importance_low, Product_importance_medium,
                  Customer_care_calls_2, Customer_care_calls_3, Customer_care_calls_4,
                  Customer_care_calls_5, Customer_care_calls_6, Customer_care_calls_7,
                  Customer_rating_1, Customer_rating_2, Customer_rating_3, Customer_rating_4,
                  Customer_rating_5, Prior_purchases_2, Prior_purchases_3, Prior_purchases_4, Prior_purchases_5,
                  Prior_purchases_6, Prior_purchases_7, Prior_purchases_8, Prior_purchases_10])
    x = x.reshape((1, -1))
    prediction = model.predict(x)
    if prediction == 1:
        return render_template('result.html', prediction="arrive late.")
    else:
        return render_template('result.html', prediction="arrive on time.")

if __name__ == "__main__":
    app.run(debug=True)

