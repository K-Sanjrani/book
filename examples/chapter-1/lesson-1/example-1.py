#!/usr/bin/env python3
"""
Example 1: Your First AI Program - Temperature Comfort Prediction
This example shows how to build a simple AI model that predicts comfort
levels based on temperature. Perfect for beginners!

Prerequisites: pip install numpy==1.24.0
"""

import numpy as np

# Step 1: Training Data
# We create a simple dataset: temperatures and their corresponding comfort levels
# Comfort level ranges from 0 (very uncomfortable) to 1 (very comfortable)
print("Setting up a simple temperature prediction model...")

# Training temperatures (in Fahrenheit)
training_temps = np.array([32, 50, 68, 75, 86, 95, 100, 45, 60, 72])

# Corresponding comfort levels (0 = very uncomfortable, 1 = perfect)
# Cold temps (< 50): low comfort
# Mild temps (50-75): high comfort
# Hot temps (> 75): medium comfort
comfort_levels = np.array([0.1, 0.3, 0.9, 0.95, 0.8, 0.6, 0.4, 0.2, 0.7, 0.92])

print(f"Training data loaded: {len(training_temps)} samples")

# Step 2: Simple Linear Model
# We'll fit a parabola to the data (since comfort peaks around 72°F)
# Using numpy's polyfit to find the best-fit polynomial

# Fit a 2nd-degree polynomial (parabola)
# This creates a curve that peaks in the middle (ideal temperatures)
coefficients = np.polyfit(training_temps, comfort_levels, 2)

print("Model trained successfully!")

# Step 3: Make Predictions
# Use the trained model to predict comfort for new temperatures
print("\nMaking predictions:")

# Test temperatures we want to predict comfort for
test_temps = np.array([75, 50, 95, 30])

# Create a polynomial function from our coefficients
# np.poly1d creates a 1D polynomial object we can use like a function
model = np.poly1d(coefficients)

# Make predictions for each test temperature
for temp in test_temps:
    # Get the prediction (ensure it stays between 0 and 1)
    prediction = max(0, min(1, model(temp)))
    print(f"Temperature: {temp}°F -> Comfort Level: {prediction:.2f}")

print("\nPredictions complete!")
