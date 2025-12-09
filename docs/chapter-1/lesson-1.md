---
title: "Your First AI Program: Building a Temperature Comfort Predictor"
description: "Create your first working AI model that learns patterns from data and makes predictions. A perfect introduction to machine learning."
sidebar_position: 1
id: "chapter-1-lesson-1"
---

# Your First AI Program: Building a Temperature Comfort Predictor

## Before this chapter

**Prerequisites**:
- Have Python 3.11+ installed ([download here](https://www.python.org/downloads/))
- Know how to run Python scripts from the command line
- Understand basic Python: variables, lists, loops, functions
- Have pip package manager available (comes with Python)

**Estimated time**: 45 minutes

---

## You will learn

By the end of this lesson, you will be able to:

1. Understand how AI models learn patterns from data
2. Create a simple machine learning model that makes predictions
3. Train a model using Python and NumPy
4. Make predictions with your trained model
5. Extend your model with more data to improve accuracy

---

## Overview

Machine learning is at the heart of modern AI. In this lesson, you'll build your first working AI program—a model that learns the relationship between temperature and human comfort levels.

**Why this matters**: Instead of hardcoding rules like "if temp > 80 then too hot," your AI model learns the pattern directly from data. This is how real-world AI systems work, from recommendation engines to autonomous vehicles.

**What we'll build**: A temperature comfort predictor that takes a temperature (in Fahrenheit) and outputs a comfort level from 0 (very uncomfortable) to 1 (perfect). The model will learn that comfort peaks around 72°F and drops at both extremes.

**The core insight**: Machine learning works in three steps:
1. **Gather data** — Collect examples of temperatures and comfort levels
2. **Train a model** — Find the mathematical relationship in the data
3. **Make predictions** — Use the model to predict comfort for new temperatures

Let's build this together!

---

## Explanation with Examples

### Core Concept 1: Training Data is Everything

Every machine learning model needs training data. The quality and quantity of data determines how well your model works.

In our case, we'll create a simple dataset: temperatures and their corresponding comfort levels. Think of it like teaching someone's preference for temperature based on past feedback.

**Example Code**:

```python title="example-1.py" showLineNumbers
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
```

**Expected output**:
```
Setting up a simple temperature prediction model...
Training data loaded: 10 samples
Model trained successfully!

Making predictions:
Temperature: 75°F -> Comfort Level: 0.83
Temperature: 50°F -> Comfort Level: 0.52
Temperature: 95°F -> Comfort Level: 0.61
Temperature: 30°F -> Comfort Level: 0.00

Predictions complete!
```

**How it works**:
- `training_temps` and `comfort_levels` are our training data
- `np.polyfit()` finds the best mathematical relationship between the two
- The model learns a parabola (curved line) that fits the data
- We then use this learned model to make predictions on new temperatures

---

### Core Concept 2: Improving Your Model with More Data

The first model works, but we can make it better by training with more data. More diverse examples help the model generalize better.

**Variation 1: Training with Extended Dataset**

```python title="example-1-variation.py" showLineNumbers
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

# Notice: With more training data, the model makes better predictions!
```

**Key insight**: More training data → Better models. This is why companies collect millions of examples to train their AI systems.

---

## Hands-On Task

**Goal**: Build and run your first AI program that makes predictions about temperature comfort.

**Instructions**:

1. **Create a new Python file** named `my_first_model.py` in a new directory:
   ```bash
   mkdir my-ai-project
   cd my-ai-project
   ```

2. **Copy the example code above** into your file, or download it from the examples folder

3. **Install NumPy** (the library we use for math):
   ```bash
   pip install numpy==1.24.0
   ```

4. **Run your program**:
   ```bash
   python example-1.py
   ```

5. **Verify the output** matches the expected output above (you should see predictions for 75°F, 50°F, 95°F, and 30°F)

6. **Experiment**: Modify the test temperatures to try your own:
   ```python
   test_temps = np.array([72, 32, 80])  # Try your own temperatures!
   ```

7. **Run the variation** to see how more data improves predictions:
   ```bash
   python example-1-variation.py
   ```

**Verification**: You've succeeded when:
- ✅ The script runs without errors
- ✅ Output shows comfort predictions for different temperatures
- ✅ You understand that comfort peaks around 72°F
- ✅ You can modify test temperatures and re-run

---

## Key Takeaways

- **Machine learning has three phases**: (1) Collect data, (2) Train model, (3) Make predictions
- **Training data drives model quality**: More diverse, higher-quality data = better predictions
- **Models learn patterns**: Your temperature model learned that comfort peaks around 72°F without hardcoding it
- **You've built your first AI program**: This is the same process used in production AI systems, just simplified
- **NumPy makes math easy**: We used polynomial fitting (a built-in function) instead of writing complex math ourselves

---

## Next Steps

Congratulations! You've built your first working AI program! 🎉

**What comes next**:

1. **Lesson 2**: Explore different types of models and when to use each one
2. **Lesson 3**: Learn how to evaluate if your model is actually working well
3. **Advanced topics**: Real datasets, neural networks, deployment to production

**Challenge project** (optional):
- Collect real comfort temperature preferences from friends
- Train your model with real-world data
- Compare predictions to actual preferences
- Share your results!

---

## Glossary

- **Training data**: Examples that teach the model patterns
- **Model**: The mathematical function learned from training data
- **Prediction**: Using the model to guess output for new input
- **NumPy**: A Python library for mathematical operations
- **Polynomial**: A curved line that fits data (like a parabola)
- **Fit**: The process of finding the best model parameters from data
