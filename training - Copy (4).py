import mediapipe as mp  # Import mediapipe
import cv2  # Import OpenCV
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score  # Accuracy metrics
import pickle

# Initialize Mediapipe Drawing and Holistic models
mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
mp_holistic = mp.solutions.holistic  # Mediapipe Solutions

# Load dataset
df = pd.read_csv('coords.csv')  # Ensure 'coords.csv' exists

# Features and target
X = df.drop('class', axis=1)  # Features (excluding 'class' column)
y = df['class']  # Target variable (class)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# Create pipelines for different algorithms
pipelines = {
    'lr': make_pipeline(StandardScaler(), LogisticRegression(max_iter=500)),
    'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier())
}

# Fit models and store them in a dictionary
fit_models = {}
for algo, pipeline in pipelines.items():
    try:
        # Fit the model
        model = pipeline.fit(X_train, y_train)
        fit_models[algo] = model
    except Exception as e:
        print(f"Error fitting model {algo}: {e}")

# Print the models to verify
print(fit_models)

# Evaluate the models and print accuracy
for algo, model in fit_models.items():
    try:
        yhat = model.predict(X_test)
        print(f"{algo} accuracy: {accuracy_score(y_test, yhat)}")
    except Exception as e:
        print(f"Error evaluating model {algo}: {e}")

# Example: Predictions with Logistic Regression (you can change the model as needed)
try:
    lr_predictions = fit_models['lr'].predict(X_test)
    print("Logistic Regression Predictions:")
    print(lr_predictions)
except KeyError:
    print("Logistic Regression model not found!")

# Save the Logistic Regression model (or any model you prefer) using pickle
try:
    with open('body_language.pkl', 'wb') as f:
        pickle.dump(fit_models.get('lr', None), f)  # Save the 'lr' model if exists
    print("Model saved as 'body_language.pkl'")
except Exception as e:
    print(f"Error saving model: {e}")
