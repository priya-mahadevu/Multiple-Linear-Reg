import streamlit as st
import util
import numpy as np


def get_location_names():
    response = util.get_location_names()
    
    return response

def predict_home_price(location,total_sqft,bhk,bath):
    total_sqft = float(total_sqft)
    location = location
    bhk = int(bhk)
    bath = int(bath)
    estimated_price=util.get_estimated_price(location,total_sqft,bhk,bath)
    return float(estimated_price)    
    
def main():
   # st.title("")
    html_temp = """
    <div style="background-color:#258820 ;padding:10px">
    <h2 style="color:white;text-align:center;">Banglore House Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    location_names = get_location_names()
    location = st.selectbox('Location', location_names, 0)
    total_sqft = st.text_input("Total SQ Feet","Type Here")
    bhk = st.text_input("BHK","Type Here")
    bath = st.text_input("BathRoom","Type Here")
    

    if st.button("House Price"):
        output=predict_home_price(location,total_sqft,bhk, bath)
        st.success('The Banglore house Price in Laks is: {}'.format(output))


if __name__=='__main__':
    util.load_saved_artifacts()
    main()


