import sqlite3
import pandas as pd


def get_hazard_data():

    data = pd.read_csv("hazard_data.csv")

    return data



def get_grazing_data():

    data = pd.read_csv("grazing_data.csv")

    return data



def get_animals():

    connection = sqlite3.connect(
        r"C:\Users\user\PyCharmMiscProject\Data\livestock.db"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM livestock")

    data = cursor.fetchall()

    connection.close()

    return data



def get_environmental_insights(location):

    grazing = pd.read_csv("grazing_data.csv")
    hazard = pd.read_csv("hazard_data.csv")


    grazing_info = grazing[
        grazing["location"] == location
    ]

    hazard_info = hazard[
        hazard["location"] == location
    ]


    insight = {

        "pasture_condition":
        grazing_info.iloc[0]["pasture_condition"],

        "water_availability":
        grazing_info.iloc[0]["water_availability"],

        "hazard":
        hazard_info.iloc[0]["hazard"],

        "risk_level":
        hazard_info.iloc[0]["risk_level"],

        "recommendation":
        hazard_info.iloc[0]["recommendation"]

    }


    return insight



def get_health_reports():

    connection = sqlite3.connect(
        "livestock.db"
    )

    cursor = connection.cursor()


    cursor.execute("""
    SELECT
    livestock.name,
    livestock.species,
    livestock.location,
    health_report.disease,
    health_report.temperature,
    health_report.status

    FROM health_report

    JOIN livestock

    ON health_report.animal_id = livestock.animal_id

    """)


    data = cursor.fetchall()

    connection.close()

    return data


