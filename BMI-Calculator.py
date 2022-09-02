
#The height and weight are needed in order to calculate the BMI
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

#This is the formula needed in order to calculate the BMI 
#The height in cm will be converted into metres by dividing the height by 100.
the_BMI = weight / (height / 100) ** 2

#The BMI rounded to 2 decimal places will be printed
print('Your Body Mass Index is {:.2f}'.format(the_BMI))

#The BMI calculator will tell you how healthy you are based on your BMI
if the_BMI <= 18.4:
    print("You are underweight.")
elif the_BMI <= 24.9:
    print("You are healthy.")
elif the_BMI <= 29.9:
    print("You are over-weight.")
elif the_BMI <= 39.9:
    print("You are obese.")
else:
    print("You are extremely obese.")

