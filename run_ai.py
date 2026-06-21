from storage import get_health_reports
from decision_engine import make_decision


reports = get_health_reports()


for animal in reports:

    name = animal[0]
    species = animal[1]
    disease = animal[2]
    temperature = animal[3]


    decision = make_decision(
        temperature,
        disease
    )


    print("----------------")
    print("Animal:", name)
    print("Species:", species)
    print("Alert:", decision["alert"])
    print("Action:", decision["action"])