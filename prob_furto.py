import streamlit as st

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import string
from fuzzywuzzy import fuzz
from sklearn.neighbors import NearestNeighbors
import warnings
warnings.filterwarnings("ignore")

# apresentar números com 3 casas decimais
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# Text/Title
st.title("Probabilidade de furto do seu veículo")

localizacao = st.text_input("Localização do Veiculo / Endereço","Digite a localização..")


all_models = ['HB20','ONIX','GOL','Saveiro']
model_choice = st.selectbox("Modelo",all_models)

ano = st.text_input("Ano de fabricação do veículo")


if st.button("Submeter"):
    st.success('Rodar modelo preditivo')
	
