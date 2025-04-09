import streamlit as st


df_data = st.session_state.data

club_options = df_data["Club"].unique().tolist()
club_selected = st.sidebar.selectbox("Time", club_options)

df_players = df_data[df_data["Club"] == club_selected]
players = df_players["Name"].unique().tolist()

player = st.sidebar.selectbox("Players", players)

player_data = df_players[df_players["Name"] == player]
player_data

st.image(player_data["Photo"].values[0])
st.title(player_data["Name"].values[0])

st.markdown(f"**Club:** {player_data['Club'].values[0]}")
st.markdown(f"**Position:** {player_data['Position'].values[0]}")
st.markdown(f"**Age:** {player_data['Age'].values[0]}")
st.markdown(f"**Nationality:** {player_data['Nationality'].values[0]}")


col1, col2, col3, col4 = st.columns(4)