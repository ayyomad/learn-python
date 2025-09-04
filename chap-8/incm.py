def inch_to_cm(inch):
    return inch * 2.54

def cm_to_inch(cm):
    return cm / 2.54

# length = input("Enter length with unit (e.g., 12in or 30cm): ").lower().replace(" ", "")

# if "inch" in length or "in" in length:
#     value = float(length.replace("inch", "").replace("in", ""))
#     result = inch_to_cm(value)
#     print(f"{length} is {result} cm")
# elif "cm" in length:
#     value = float(length.replace("cm", ""))
#     result = cm_to_inch(value)
#     print(f"{length} is {result} inch")
# else:
#     print("Invalid input. Please specify the unit as 'in', 'inch', or 'cm'.")



len=input("enter the length with unit: ").lower().replace(" ","")

if "inch" in len or "in" in len:
    val=float(len.replace("inch","").replace("in",""))
    print(f"{len} is {round(inch_to_cm(val),3)} cm ")

elif "cm" in len:
    val=float(len.replace("cm",""))
    print(f"{len} is {round(cm_to_inch(val),3)} inch")


''