import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Inventory Management System")

st.header("Add Product")

name = st.text_input("Product Name")
price = st.number_input("Price",min_value=0)
if st.button("Add Product"):
    data = {'name': name,'price':price}
    response = requests.post(f"{API_URL}/product",json=data)

    if response.status_code == 200:
        st.success("Product added!")

    else:
        st.error("Error adding product")


st.header("All Products")
if st.button("Load Products"):
    response = requests.get(f"{API_URL}/product") 
    if response.status_code == 200:
        products = response.json()
        st.dataframe(products)

    else:
        st.error("Failed to fecth products")



st.header("Update Product")

update_id = st.number_input("Product ID to update",min_value=1)
new_name = st.text_input("New Name")
new_price = st.number_input("New Price",min_value=0)

if st.button('Update Product'):
    data = {"name": new_name, "price": new_price}
    response = requests.put(f"{API_URL}/product/{update_id}",json=data)
    if response.status_code == 200:
        st.success("Updated Successfully")

    else:
        st.error("Update Failed")


st.header("Delete Product")
product_id = st.number_input("Product Id to delete",min_value=1)
if st.button("Delete Product"):
    data = {'product_id':product_id}
    response = requests.delete(f"{API_URL}/product/{product_id}",json=data)
    if response.status_code == 200:
        st.success("Product deleted successfully")

    else:
        st.error("Failded to delete")