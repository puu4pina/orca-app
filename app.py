import streamlit as st

st.set_page_config(page_title="Miekkavalas-peli")

if "stage" not in st.session_state:
    st.session_state.stage = 0

st.title("🐋 Miekkavalas-peli")

# First question
if st.session_state.stage == 0:

    st.header("Tykkäätkö miekkavalaista")

    col1, col2 = st.columns(2)

    if col1.button("✅ Joo"):
        st.session_state.stage = 999
        st.rerun()

    if col2.button("❌ En"):
        st.session_state.stage = 1
        st.rerun()

# Game over
elif st.session_state.stage == 999:

    st.error("GAME OVER")
    st.write(".....")

    if st.button("Yritä uudelleen"):
        st.session_state.stage = 0
        st.rerun()

# Other questions
elif st.session_state.stage == 1:

    st.header("Pitäisikö miekkavalaiden maksaa veroja?")

    col1, col2 = st.columns(2)

    if col1.button("✅ Joo"):
        st.session_state.stage = 2
        st.rerun()

    if col2.button("❌ Ei"):
        st.session_state.stage = 2
        st.rerun()

elif st.session_state.stage == 2:

    st.header("Ajaako miekkavalaat trukkia?")

    col1, col2 = st.columns(2)

    if col1.button("✅ Joo"):
        st.session_state.stage = 3
        st.rerun()

    if col2.button("❌ Ei"):
        st.session_state.stage = 3
        st.rerun()

# Final question
elif st.session_state.stage == 3:

    st.header("Viimenen kyssäri")
    st.subheader("Onko miekkavalaat hauskoja?")

    col1, col2 = st.columns(2)

    if col1.button("✅ Joo"):
        st.session_state.stage = 4
        st.rerun()

    if col2.button("❌ Ei"):
        st.success("🏆 Voitit!")
        st.balloons()

# Punishment for saying yes
elif st.session_state.stage == 4:

    st.header("Väärin.")
    st.write("Yritä uudelleen.")

    col1, col2 = st.columns(2)

    if col1.button("❌ Ei", key="n1"):
        st.success("🏆 Voitit!")
        st.balloons()

    if col2.button("❌ Ei", key="n2"):
        st.success("🏆 Voitit!")
        st.balloons()