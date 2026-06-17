import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("fertilizer.csv")

# Encode categorical columns
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

df["Soil_Type"] = le_soil.fit_transform(df["Soil_Type"])
df["Crop_Type"] = le_crop.fit_transform(df["Crop_Type"])
df["Fertilizer_Name"] = le_fert.fit_transform(df["Fertilizer_Name"])

X = df.drop("Fertilizer_Name", axis=1)
y = df["Fertilizer_Name"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model & encoders
pickle.dump(model, open("fertilizer_model.pkl", "wb"))
pickle.dump(le_soil, open("soil_encoder.pkl", "wb"))
pickle.dump(le_crop, open("crop_encoder.pkl", "wb"))
pickle.dump(le_fert, open("fertilizer_encoder.pkl", "wb"))

print("✅ Fertilizer Model Saved Successfully")