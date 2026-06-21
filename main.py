import streamlit as st
import pandas as pd

from storage import get_health_reports, get_hazard_data, get_grazing_data
from decision_engine import make_decision


st.title(" Smart Pastoral AI Livestock Monitoring System")


reports = get_health_reports()

hazards = pd.read_csv("hazard_zones.csv")
grazing = pd.read_csv("grazing_data.csv")


for animal in reports:

    name = animal[0]
    species = animal[1]
    location = animal[2]

    st.write("Animal location:", location)

    disease = animal[3]
    temperature = animal[4]
    status = animal[5]


    decision = make_decision(
        temperature,
        disease
    )


    st.subheader(f" {name} ({species})")

    st.write("Disease:", disease)
    st.write("Temperature:", temperature)
    st.write("Status:", status)


    if decision["alert"] == "CRITICAL":
        st.error(decision["alert"])

    elif decision["alert"] == "WARNING":
        st.warning(decision["alert"])

    else:
        st.success(decision["alert"])


    st.write("Recommendation:", decision["action"])
    st.subheader("Environmental Insights")

    hazard = hazards[
        hazards["location"].str.strip() == location.strip()
        ]

    grazing_info = grazing[
        grazing["location"].str.strip() == location.strip()
        ]

    if not hazard.empty and not grazing_info.empty:

        st.write("Pasture Condition:",
                 grazing_info.iloc[0]["pasture_condition"])

        st.write("Water Availability:",
                 grazing_info.iloc[0]["water_availability"])

        st.write("Hazard:",
                 hazard.iloc[0]["hazard"])

        st.write("Risk Level:",
                 hazard.iloc[0]["risk_level"])

        st.write("Recommendation:",
                 hazard.iloc[0]["recommendation"])

    else:
        st.write("Environmental data not available")



   

    st.divider()