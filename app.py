import streamlit as st
import time

st.set_page_config(page_title="Mitä tapahtuu jos kyykkää 10 kertaa?", layout="wide")

# --- SESSION STATE INITIALISATION ---
if "state" not in st.session_state:
    st.session_state.state = "seiso"  # seiso / kyykkaa
if "last_squat_time" not in st.session_state:
    st.session_state.last_squat_time = 0
if "squats" not in st.session_state:
    st.session_state.squats = 0
if "fact_index" not in st.session_state:
    st.session_state.fact_index = -1  # first fact appears after 10 squats

# --- ASSETS ---
standing_img = "standing.png"
squatting_img = "squatting.png"

# --- ORCA FACTS (FINNISH) ---
facts = [
    "Orkat ovat maailman suurimpia kiusaajia.",
    "Orkat ovat huippupetoja, joilla ei ole luonnollisia vihollisia.",
    "Orkat voivat elää yli 80‑vuotiaiksi. Kammottavaa!",
    "Orkat mukauttavat ja opettavat metsästystekniikoita jälkeläisilleen.",
    "Orkat voivat uida jopa 55 km/h. Itse uisin nopeammin.",
    "Orkat tunnistavat oman heimonsa äänistä. Yeah right...",
    "Orkat ovat yksi maailman älykkäimmistä eläinlajeista. Doubt it."
]


# --- MAIN UPDATE LOGIC ---
def update_squat_state():
    now = time.time()

    # Auto-stand up after 1 sec
    if st.session_state.state == "kyykkaa":
        if now - st.session_state.last_squat_time > 1:
            st.session_state.state = "seiso"


# --- UI ---
st.title("Mitä tapahtuu jos kyykkää 10 kertaa?")

# Show counter
st.markdown(f"## Kyykkyjä yhteensä: **{st.session_state.squats}**")

# Electrician image
if st.session_state.state == "seiso":
    st.image(standing_img, width=180)
else:
    st.image(squatting_img, width=180)

# Squat button
if st.button("KYYKKÄÄ"):
    st.session_state.state = "kyykkaa"
    st.session_state.last_squat_time = time.time()
    st.session_state.squats += 1

    # Every 10 squats → new orca fact
    if st.session_state.squats % 10 == 0:
        st.session_state.fact_index += 1
        if st.session_state.fact_index >= len(facts):
            st.session_state.fact_index = 0  # loop facts endlessly

# Show orca fact if any reached
if st.session_state.fact_index >= 0:
    st.markdown("### 🐳 Orkafakta:")
    st.markdown(f"**{facts[st.session_state.fact_index]}**")

# Update character pose
update_squat_state()

# Smooth small loop effect
time.sleep(0.05)
st.rerun()
