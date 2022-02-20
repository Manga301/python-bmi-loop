
def bmi_calc(weight, height):
    bmi = round(weight / (height * height))

    if bmi < 18.5:
        print(f"Your BMI is ({bmi}), you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is ({bmi}), you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is ({bmi}), you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is ({bmi}), you are obese.")
    else:
        print(f"Your BMI is ({bmi}), you are clinically obese.")
        
    return bmi


continue_bmi_test = True

while continue_bmi_test == True:
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    
    result = bmi_calc(weight, height)
    print(result)
    
    continue_check = input("Continue? 'y' or 'n'")

    if continue_check == "y":
        result
    elif continue_check == "n":
        print("Goodbye!")
        continue_bmi_test = False
    else:
        print("Invalid input, goodbye!")
        continue_check = False
        
    

