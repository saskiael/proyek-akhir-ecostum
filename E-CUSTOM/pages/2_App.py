import streamlit as st 
import pandas as pd
import numpy as np
import time
from function import PLD
from function import PPM
from function import Gen
from function import POC
from function import MS
import matplotlib.pyplot as plt    
import pickle
import os

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image : url(https://i.pinimg.com/564x/bf/20/62/bf2062653ee6816525b7711b8b1cdff5.jpg);
background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"]{
right: 2rem;
}

[data-testid="stSidebar"]{
background-color: color-mix(in oklab, blue 30%, white 70%);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

with st.container():


    Tenure = st.number_input('**Tenure:** ', 0)
    PreferredLoginDevice = st.selectbox('**Apa perangkat yang digunakan:** ',('Mobile Phone', 'Phone','Computer'))
    PreferredLoginDevice = PLD(PreferredLoginDevice)
    CityTier = st.number_input('**CityTier:** ', 0)
    WarehouseToHome =  st.number_input('**WarehouseToHome:** ',0)
    PreferredPaymentMode = st.selectbox('**Metode pembayaran:** ',('Debit Card','UPI' ,'CC', 'Cash on Delivery', 'E wallet', 'COD', 'Credit Card'))
    PreferredPaymentMode = PPM(PreferredPaymentMode)
    Gender = st.selectbox('**Apa Jenis kelamin Anda:** ',('Male','Female'))
    Gender = Gen(Gender)
    HourSpendOnApp = st.number_input('**Hour Spend On App:** ',0)
    NumberOfDeviceRegistered =st.number_input('**Number Of Device Registered:** ',0)
    PreferedOrderCat =  st.selectbox('**Order:** ',('Laptop & Accessory', 'Mobile', 'Mobile Phone', 'Fashion', 'Others', 'Grocery'))
    PreferedOrderCat = POC(PreferedOrderCat)
    SatisfactionScore =st.number_input('**Satis faction Score:** ',0)
    MaritalStatus =  st.selectbox('**Status:** ',('Single', 'Divorced', 'Married'))
    MaritalStatus = MS(MaritalStatus)
    NumberOfAddress	 =st.number_input('**Number Of Address:** ',0)
    Complain	 =st.number_input('**Complain:** ',0)
    OrderAmountHikeFromlastYear  = st.number_input('**Order Amount Hike From last Year:** ',0)
    CouponUsed	 = st.number_input('**Coupon Used:** ',0)
    OrderCount	 = st.number_input('**Order Count:** ',0)
    DaySinceLastOrder	 = st.number_input('**DaySince Last Order:** ',0)
    CashbackAmount = st.number_input('**Cashback Amount(100-300):** ',0)

    submit_button = st.button('Predict')

    if submit_button:
            # Load Pikle File Model dan Scaler
            with open('scaler.pkl', "rb") as file1:
                scaler = pickle.load(file1)
            with open('model.pkl', "rb") as file2:
                model = pickle.load(file2)
                
            # data baru yang diinput harus di-standardization terlebih dahulu
            data_baru = [[Tenure,	PreferredLoginDevice,	CityTier,	WarehouseToHome,	PreferredPaymentMode,	Gender,	HourSpendOnApp,	NumberOfDeviceRegistered,	PreferedOrderCat,	SatisfactionScore,	MaritalStatus,	NumberOfAddress,	Complain,	OrderAmountHikeFromlastYear,	CouponUsed	,OrderCount,	DaySinceLastOrder, CashbackAmount]]
            data_baru = scaler.transform(data_baru)

            # prediksi data baru, yang sudah di-standardization, menggunakan model SVM terbaik
            hasil_prediksi = model.predict(data_baru)
            hasil_prediksi = int(hasil_prediksi)
            

            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()


            st.write('Hasil prediksi index Anda adalah ', end='')
            if hasil_prediksi == 0:
              st.success('Tidak Churn')
            else :
              st.error('Churn')