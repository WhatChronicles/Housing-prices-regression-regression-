import streamlit as st
import pandas as pd

def user_input_form():
    st.subheader("Enter house features to predict SalePrice")
    grlivarea = st.number_input("Above grade living area (sqft)", min_value=200, max_value=6000, value=1500, step=10)
    totrmsabvgrd = st.number_input("Total rooms above grade", min_value=1, max_value=20, value=6, step=1)
    fullbath = st.number_input("Full baths", min_value=0, max_value=5, value=2, step=1)
    halfbath = st.number_input("Half baths", min_value=0, max_value=5, value=1, step=1)
    neighborhood = st.selectbox("Neighborhood", ["NAmes","CollgCr","OldTown","Edwards","Somerst","Sawyer","NridgHt","Other","Missing"])
    overallqual = st.slider("Overall quality (1-10)", min_value=1, max_value=10, value=6)
    yearbuilt = st.number_input("Year built", min_value=1872, max_value=2010, value=1995, step=1)

    total_baths = fullbath + 0.5 * halfbath
    area_per_room = grlivarea / max(totrmsabvgrd, 1)

    df = pd.DataFrame([{
        "grlivarea": grlivarea,
        "totrmsabvgrd": totrmsabvgrd,
        "fullbath": fullbath,
        "halfbath": halfbath,
        "neighborhood": neighborhood,
        "overallqual": overallqual,
        "yearbuilt": yearbuilt,
        "total_baths": total_baths,
        "area_per_room": area_per_room
    }])
    return df