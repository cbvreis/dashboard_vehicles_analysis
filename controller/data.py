import streamlit as st
from database import Database

@st.cache(allow_output_mutation=True)
def load_data():
    '''
    Load data from sqlite3 and convert to dataframe pandas
    :return: dataframe pandas
    '''
    data_base = Database()
    data_base.connect()
    df = data_base.read_pandas()
    #df_cons = data_base.read_pandas_consumo()
    #return df,df_cons
    return df
