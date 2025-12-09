#!/usr/bin/env python3
"""
Variation 1: Improving the Model with More Data

This variation shows how to train the model with more data points,
making predictions more accurate. The key difference is that we can
add more training samples to improve model quality.

Prerequisites: pip install numpy==1.24.0
"""

import numpy as np

print("Building a better temperature prediction model with more data...")

# VARIATION: Extended training dataset
# More data points = better model
training_temps = np.array([
    32, 40, 50, 60, 68, 72, 75, 80, 86, 90, 95, 100,
    45, 55, 65, 70, 78, 88
])

comfort_levels = np.array([
    0.1, 0.2, 0.3, 0.6, 0.85, 0.95, 0.92, 0.85, 0.7, 0.6, 0.4, 0.2,
    0.25, 0.5, 0.8, 0.90, 0.8, 0.5
])

print(f"Training data loaded: {len(training_temps)} samples (improved from 10)")

# Train the model with more data
coefficients = np.polyfit(training_temps, comfort_levels, 2)
print("Model trained with more data!")

# Make predictions
print("\nMaking predictions with improved model:")

test_temps = np.array([72, 68, 95, 50])
model = np.poly1d(coefficients)

for temp in test_temps:
    prediction = max(0, min(1, model(temp)))
    print(f"Temperature: {temp}°F -> Comfort Level: {prediction:.2f}")

print("\nNotice: With more training data, the model makes better predictions!")
