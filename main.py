height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

bmi = weight/height ** 2
bmi_rounded = round(bmi, 2)


if bmi < 18.5:
  print(f"Your BMI is {bmi_rounded}, you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi_rounded}, you are normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi_rounded}, you are overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi_rounded}, you are obese")
elif bmi > 35:
  print(f"Your BMI is {bmi_rounded}, you are clinically obese")
