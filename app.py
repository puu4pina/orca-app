import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Mikä valas olet?",
    page_icon="🐋",
    layout="centered"
)

# --- Hero section ---
st.image("hero.jpg", use_container_width=True)
st.title("🐋 Mikä valas matchaa persoonallisuuttasi parhaiten?")
st.subheader("Vastaa muutamaan kysymykseen ja selvitä tulos 👇")

st.write("---")

# --- Initialize scores ---
scores = {
    "ryhävalas": 0,
    "sinivalas": 0,
    "beluga": 0,
    "orca": 0
}

# --- Questions ---
st.markdown("### 1️⃣ Nautitko muiden auttamisesta?")
q1 = st.radio(
    "",
    ["Usein", "Joskus", "Harvoin", "En koskaan"],
    index=0
)

st.markdown("### 2️⃣ Kuinka hyvin hallitset stressiä?")
q2 = st.radio(
    "",
    ["Erittäin hyvin", "Kohtalaisesti", "Huonosti", "En hallitse ollenkaan"],
    index=0
)

st.markdown("### 3️⃣ Miten suhtaudut konflikteihin?")
q3 = st.radio(
    "",
    ["Yritän sovitella", "Vältän", "Puolustaudun aggressiivisesti", "Haen konflikteja"],
    index=0
)

st.markdown("### 4️⃣ Koetko usein vihaa tai kyynisyyttä?")
q4 = st.radio(
    "",
    ["Harvoin", "Joskus", "Usein", "Lähes aina"],
    index=0
)

# --- Scoring logic ---
def apply_scores():
    # Q1
    if q1 == "Usein":
        scores["ryhävalas"] += 2
        scores["beluga"] += 1
    elif q1 == "Joskus":
        scores["sinivalas"] += 1
    elif q1 == "Harvoin":
        scores["orca"] += 1
    else:
        scores["orca"] += 2

    # Q2
    if q2 == "Erittäin hyvin":
        scores["sinivalas"] += 2
    elif q2 == "Kohtalaisesti":
        scores["ryhävalas"] += 1
    elif q2 == "Huonosti":
        scores["orca"] += 1
    else:
        scores["orca"] += 2

    # Q3
    if q3 == "Yritän sovitella":
        scores["ryhävalas"] += 2
    elif q3 == "Vältän":
        scores["beluga"] += 1
    elif q3 == "Puolustaudun aggressiivisesti":
        scores["orca"] += 2
    else:
        scores["orca"] += 3

    # Q4
    if q4 == "Harvoin":
        scores["sinivalas"] += 2
    elif q4 == "Joskus":
        scores["beluga"] += 1
    elif q4 == "Usein":
        scores["orca"] += 2
    else:
        scores["orca"] += 3

# --- Result button ---
st.write("---")
if st.button("🔍 Näytä tulos"):
    apply_scores()
    result = max(scores, key=scores.get)

    st.write("## 🎉 Tuloksesi:")

    if result == "ryhävalas":
        st.image("whale1.png", use_container_width=True)
        st.subheader("🐋 Ryhävalas")
        st.write(
            "Olet luova, empaattinen ja arvostat yhteyttä muihin. "
            "Sinulla on vahva tunneäly ja kyky nähdä kauneutta siellä missä muut eivät."
        )

    elif result == "sinivalas":
        st.image("whale2.png", use_container_width=True)
        st.subheader("🐋 Sinivalas")
        st.write(
            "Huokut rauhallista voimaa ja itsevarmuutta. "
            "Et tarvitse draamaa – tiedät kuka olet ja kannat sen arvokkaasti."
        )

    elif result == "beluga":
        st.image("whale3.png", use_container_width=True)
        st.subheader("🐋 Beluga")
        st.write(
            "Olet leikkisä, utelias ja sosiaalinen. "
            "Tuot iloa ympärillesi ja uskallat näyttää tunteesi avoimesti."
        )

    else:
        st.image("whale4.png", use_container_width=True)
        st.subheader("🐋 Miekkavalas (Orca)")
        st.write(
            "Olet dominoiva, kylmä ja äärimmäisen määrätietoinen. "
            "Maailma on sinulle taistelukenttä – ja sinä aiot voittaa."
        )

    st.write("---")
    st.caption("Tämä testi on tieteellisesti vedenpitävä")
