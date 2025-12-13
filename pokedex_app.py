"""
MIT License

Copyright (c) 2025 SRINJOY DAS 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pokémon Search", layout="wide")
st.title("🔍 Pokémon Search")

@st.cache_data
def load_data():
    return pd.read_csv("pokemon.csv")

df = load_data()

# ---------- TYPE COLORS ----------
TYPE_COLORS = {
    "Fire": "#F08030",
    "Water": "#6890F0",
    "Grass": "#78C850",
    "Electric": "#F8D030",
    "Ice": "#98D8D8",
    "Fighting": "#C03028",
    "Poison": "#A040A0",
    "Ground": "#E0C068",
    "Flying": "#A890F0",
    "Psychic": "#F85888",
    "Bug": "#A8B820",
    "Rock": "#B8A038",
    "Ghost": "#705898",
    "Dragon": "#7038F8",
    "Dark": "#705848",
    "Steel": "#B8B8D0",
    "Fairy": "#EE99AC",
    "Normal": "#A8A878"
}

search = st.text_input("Enter Pokémon name :")

if search:
    results = df[df["Name"].str.contains(search, case=False, na=False)]

    if results.empty:
        st.error("❌ No Pokémon found")
    else:
        st.success(f"Found {len(results)} Pokémon")

        for _, row in results.iterrows():
            with st.container(border=True):

                col1, col2 = st.columns([1, 3])

                # ---------- IMAGE ----------
                with col1:
                    poke_id = int(row["#"])
                    img_url = (
                        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
                        f"sprites/pokemon/other/official-artwork/{poke_id}.png"
                    )
                    st.image(img_url, width=200)

                # ---------- DETAILS ----------
                with col2:
                    type1 = row["Type 1"]
                    name_color = TYPE_COLORS.get(type1, "#FFFFFF")

                    # COLORED NAME
                    st.markdown(
                        f"<h2 style='color:{name_color};'>{row['Name']}</h2>",
                        unsafe_allow_html=True
                    )

                    st.write(
                        f"**Type:** {type1}"
                        f"{'' if pd.isna(row['Type 2']) else ' / ' + row['Type 2']}"
                    )

                    st.write(f"**Total:** {row['Total']}")
                    st.write(f"**Generation:** {row['Generation']}")
                    st.write(
                        f"**Legendary:** {'Yes 🔥' if row['Legendary'] else 'No'}"
                    )

                    st.markdown("### Stats")
                    stat_col1, stat_col2, stat_col3 = st.columns(3)

                    stat_col1.metric("HP", row["HP"])
                    stat_col1.metric("Attack", row["Attack"])

                    stat_col2.metric("Defense", row["Defense"])
                    stat_col2.metric("Sp. Atk", row["Sp. Atk"])

                    stat_col3.metric("Sp. Def", row["Sp. Def"])
                    stat_col3.metric("Speed", row["Speed"])


st.markdown("---")
st.markdown("Developed by Srinjoy Das")

