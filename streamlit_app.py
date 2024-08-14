import streamlit as st
import pandas as pd

# Carrega os arquivos Excel
file1 = st.file_uploader("Selecione a primeira planilha Excel", type=["xlsx"])
file2 = st.file_uploader("Selecione a segunda planilha Excel", type=["xlsx"])

# Se os arquivos foram carregados
if file1 is not None and file2 is not None:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Mostra os nomes das colunas de cada planilha
    st.write("Nomes das colunas na primeira planilha:")
    st.write(df1.columns)

    st.write("Nomes das colunas na segunda planilha:")
    st.write(df2.columns)

    # Identifica quais campos podem ser usados para fazer um lookup
    st.write("Campos possíveis para criar um lookup entre as duas planilhas:")
    possible_fields = set(df1.columns).intersection(set(df2.columns))
    st.write(possible_fields)
