import sys
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
if weight <= 0 or height <= 0:
    print("Invalid input. Please enter positive values for weight and height.")
    sys.exit()  
bmi = weight / (height ** 2)
print("Your BMI: {:.2f}".format(bmi))
    
def classify_bmi(weight, height):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
category = classify_bmi(weight, height)

print(f"Your BMI category is: {category}")