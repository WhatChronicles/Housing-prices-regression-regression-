import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def eda_section(df: pd.DataFrame):
    st.subheader("EDA")
    st.write("Shape:", df.shape)
    st.write(df.dtypes)
    st.write(df.describe(include="all"))

    if "saleprice" in df.columns:
        fig, ax = plt.subplots()
        sns.boxplot(x=df["saleprice"], ax=ax)
        ax.set_title("SalePrice distribution")
        st.pyplot(fig)

    if "neighborhood" in df.columns:
        fig, ax = plt.subplots(figsize=(10,4))
        sns.countplot(data=df, x="neighborhood", ax=ax, order=df["neighborhood"].value_counts().index)
        ax.set_title("Neighborhood counts")
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    if set(["grlivarea","saleprice"]).issubset(df.columns):
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="grlivarea", y="saleprice", ax=ax)
        ax.set_title("Living area vs SalePrice")
        st.pyplot(fig)