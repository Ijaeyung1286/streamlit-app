import streamlit as st
import pandas as pd
import numpy as np

st.header("Learn Streamlit!")



df = pd.DataFrame(
    np.random.randn(200,3),
    columns=["a","b","c"]
)

st.write(df)
