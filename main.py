import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

def main():
    html_temp = """
<div style="background-color: #E6E6FA; padding: 16px; border-radius: 8px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.2);">
    <h2 style="color: #333333; text-align: center; font-size: 24px; margin-bottom: 16px; text-transform: uppercase;">Credit Card Fraud Prediction Using ML</h2>
</div>
"""
    st.markdown(html_temp, unsafe_allow_html=True)
    model = joblib.load('credit_card_model')
    v1 = st.slider("Enter value for v1", 0.0, 1.0, step=0.01, key="slider1")
    v2 = st.slider("Enter value for v2", 0.0, 1.0, step=0.01, key="slider2")
    v3 = st.slider("Enter value for v3", 0.0, 1.0, step=0.01, key="slider3")
    v4 = st.slider("Enter value for v4", 0.0, 1.0, step=0.01, key="slider4")
    v5 = st.slider("Enter value for v5", 0.0, 1.0, step=0.01, key="slider5")
    v6 = st.slider("Enter value for v6", 0.0, 1.0, step=0.01, key="slider6")
    v7 = st.slider("Enter value for v7", 0.0, 1.0, step=0.01, key="slider7")
    v8 = st.slider("Enter value for v8", 0.0, 1.0, step=0.01, key="slider8")
    v9 = st.slider("Enter value for v9", 0.0, 1.0, step=0.01, key="slider9")
    v10 = st.slider("Enter value for v10", 0.0, 1.0, step=0.01, key="slider10")
    v11 = st.slider("Enter value for v11", 0.0, 1.0, step=0.01, key="slider11")
    v12 = st.slider("Enter value for v12", 0.0, 1.0, step=0.01, key="slider12")
    v13 = st.slider("Enter value for v13", 0.0, 1.0, step=0.01, key="slider13")
    v14 = st.slider("Enter value for v14", 0.0, 1.0, step=0.01, key="slider14")
    v15 = st.slider("Enter value for v15", 0.0, 1.0, step=0.01, key="slider15")
    v16 = st.slider("Enter value for v16", 0.0, 1.0, step=0.01, key="slider16")
    v17 = st.slider("Enter value for v17", 0.0, 1.0, step=0.01, key="slider17")
    v18 = st.slider("Enter value for v18", 0.0, 1.0, step=0.01, key="slider18")
    v19 = st.slider("Enter value for v19", 0.0, 1.0, step=0.01, key="slider19")
    v20 = st.slider("Enter value for v20", 0.0, 1.0, step=0.01, key="slider20")
    v21 = st.slider("Enter value for v21", 0.0, 1.0, step=0.01, key="slider21")
    v22 = st.slider("Enter value for v22", 0.0, 1.0, step=0.01, key="slider22")
    v23 = st.slider("Enter value for v23", 0.0, 1.0, step=0.01, key="slider23")
    v24 = st.slider("Enter value for v24", 0.0, 1.0, step=0.01, key="slider24")
    v25 = st.slider("Enter value for v25", 0.0, 1.0, step=0.01, key="slider25")
    v26 = st.slider("Enter value for v26", 0.0, 1.0, step=0.01, key="slider26")
    v27 = st.slider("Enter value for v27", 0.0, 1.0, step=0.01, key="slider27")
    v28 = st.slider("Enter value for v28", 0.0, 1.0, step=0.01, key="slider28")
    v29 = st.slider("Enter value for v29", 0.0, 1.0, step=0.01, key="slider29")

    if st.button('Predict'):
        pred=model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,
                               v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29]])
        
        st.balloons()
        if pred == 0:
            st.write("<h3 style='color:green;'>Normal Transcation</h3>", unsafe_allow_html=True)
        else:
            st.write("<h3 style='color:yellow;'>Fraudulent Transcation</h3>", unsafe_allow_html=True)
        st.write("You entered:", v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29)
        st.success('Thank You')

if __name__ == '__main__':
    main()