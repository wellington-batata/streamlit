from datetime import datetime
import streamlit as st
import webbrowser
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("data/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values("Overall", ascending=False)
    st.session_state.data = df_data

st.markdown("# FIFA 2023 OFFICIAL DATAASET")

st.sidebar.markdown("Desenvolvido por BatataDev")

btn = st.button("Acesso a base de dados no Kaggle")

if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset")

st.markdown(
    """
    Os conjuntos de dados fornecidos incluem os jogadores datam do modo de carreira do FIFA 15 a FIFA 23. Os dados permitem comparação múltipla para os mesmos jogadores nas últimas 9 versões do videogame.
    """,
    unsafe_allow_html=True,
)
