import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle


# Load dataset
data = pd.read_csv("../../grazing_data.csv")
print(data.head())


# Convert text values into numbers

data["vegetation"] = data["vegetation"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

data["water_access"] = data["water_access"].map({
    "Far": 0,
    "Near": 1
})

data["terrain_safety"] = data["terrain_safety"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})


# Features
X = data[
    [
        "temperature",
        "vegetation",
        "water_access",
        "terrain_safety"
    ]
]


# Output
y = data["recommendation"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = DecisionTreeClassifier()


# Train
model.fit(X_train, y_train)


# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)


# Save model
with open("../models/grazing_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model saved successfully!")