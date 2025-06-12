import streamlit as st
import pandas as pd
import numpy as np

st.title("hello sajan")
st.write("this is a simple text")
df=pd.DataFrame({
    "first":[1,2,3,4],
    "second":[6,7,8,9]}
)
st.write("here is the dataframe")
st.write(df)


df=pd.DataFrame(
    np.random.randn(20,3),columns=["a","s","d"]
)
st.write("line chart")
st.line_chart(df)

    