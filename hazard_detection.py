import pandas as pd
from decision_engine import make_decision

animals = pd.read_csv("../../livestock_data.csv")
hazards = pd.read_csv("../../hazard_zones.csv")

print("==============================")
print(" OFFLINE SMART PASTORAL AI ")
print("==============================")


for index, animal in animals.iterrows():

    animal_zone = animal["zone"]

    if animal_zone in hazards["zone"].values:

        risk = hazards[
            hazards["zone"] == animal_zone
        ]["risk"].values[0]

        if risk == "High":

            decision = make_decision("High Risk")



            print("Animal ID:", animal["animal_id"])
            print("Location:", animal_zone)

            print("Risk Level:", risk)

            print("Status:", decision["alert"])

            print("AI Recommendation:")
            print(decision["action"])

            print("==============================")


        elif risk == "Medium":

            decision = make_decision("Medium Risk")

            print("\nWARNING")
            print("Animal ID:", animal["animal_id"])
            print("Location:", animal_zone)

            print("Status:", decision["alert"])
            print("Action:", decision["action"])


        else:

            decision = make_decision("Safe")

            print(
                animal["animal_id"],
                decision["action"]
            )