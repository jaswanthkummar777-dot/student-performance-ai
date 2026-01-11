import numpy as np

# Training data: [study hours] → [marks]
X = np.array([1,2,3,4,5,6,7,8,9,10])
Y = np.array([35,40,50,55,60,65,70,78,85,92])

# Simple AI model (Linear Regression)
m, b = np.polyfit(X, Y, 1)

def predict_marks(hours):
    return m * hours + b

print("AI Student Performance Predictor")
hours = float(input("Enter study hours per day: "))
prediction = predict_marks(hours)

print("Predicted Score:", round(prediction,2), "%")

if prediction < 50:
    print("Advice: Increase study time and revise fundamentals.")
elif prediction < 75:
    print("Advice: Good, but more practice will help.")
else:
    print("Excellent performance expected!")
