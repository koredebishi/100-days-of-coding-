# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round ((weight / (height ** 2)),2)
print ("Your BMI is: ", bmi)

if bmi < 18.5: 
  print("You are Underweight")
elif bmi < 25:
  print ("Your BMI is Normal:")
elif bmi < 30 :
  print ("You are slightly Overwight")
elif bmi < 35:
  print ("You are obese") 

else:
  print (f"Your bmi is {bmi}, you are clinically Obese")

  



