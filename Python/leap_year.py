# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 ==0 and year % 400 == 0:
#     print("leap year")

if year % 4 == 0 or year % 400 == 0:
    print("leap")
else:
    print("not leap year")
