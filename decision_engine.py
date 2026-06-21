def make_decision(temperature, disease):

    if temperature >= 40:
        return {
            "alert": "CRITICAL",
            "action": "Check animal health and provide shelter"
        }

    elif disease != "Normal":
        return {
            "alert": "WARNING",
            "action": "Monitor animal closely"
        }

    else:
        return {
            "alert": "SAFE",
            "action": "Continue normal grazing"
        }