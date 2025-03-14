import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("phishing_data.csv")

# Select features and labels
X = df.drop(columns=['CLASS_LABEL', 'id'])  # Remove 'id' and target column
y = df['CLASS_LABEL']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model training complete. Model saved.")
