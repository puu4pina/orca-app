import streamlit as st

# List of true orca facts in Finnish
facts = [
    "Sehän on vain yleistietoa, että miekkavalaat (orkat) ovat itse asiassa suuria delfiineitä, eivät valaita.",
    "Näin yhdestä videosta, että orkat elävät tiiviissä perheryhmissä, joita kutsutaan podeiksi.",
    "Kaveri kertoi, että niillä on erittäin kehittynyt kommunikaatio ja omia 'murteita'.",
    "Kuulin podcastista, että orkat voivat uida jopa noin 50 km/h nopeudella.",
    "On synkkää ja kamalaa, että ne  ovat huippupetoja, joilla ei ole luonnollisia vihollisia. Ne kiusaavat söpöjä hylkeitä ja toisia valaita."
]

# Initialize session state counter
if "count" not in st.session_state:
    st.session_state.count = 0

st.title("🐋 Miekkavalaat")

# Show your uploaded image
st.image("orca.jpg", caption="Miekkavalas", use_container_width=True)

# Button
if st.button("Klikkaa tästä"):
    st.session_state.count += 1

# Show fact (looping)
if st.session_state.count > 0:
    index = (st.session_state.count - 1) % len(facts)
    st.write(facts[index])