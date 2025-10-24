
import streamlit as st
import requests

st.title("Sales Predicter - Craig Murray") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.000001, value=1.0) 
Product_MRP = st.number_input("Product MRP", min_value=1.0, value=300.0)
Store_Id = st.selectbox("Store ID", ["OUT001", "OUT002", "OUT003", "OUT004",]) 
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"]) 
Store_Type = st.selectbox("Store Type", ["Supermarket Type2", "Departmental Store", "Supermarket Type1", "Food Mart"])
Product_Type_4 = st.selectbox("Product_Type_4", ["drinks", "perishable", "nonperishable", "others"]) 


product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Id" : Store_Id,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Type_4": Product_Type_4,
}

if st.button("Predict", type='primary'):
    response = requests.post("https://cmurray4492-superkart.hf.space/v1/predict", json=product_data)
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")
