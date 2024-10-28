from datetime import datetime

def day_difference(date1, date2):
    #Convert dates to daytime format
    date1 = datetime.strptime(date1, "%d-%m-%Y")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    #calculate the day difference using the timedelta
    dif = abs(date2 - date1)
    return dif.days

#using function
date1 = "1-10-2024"
date2 = "2024-10-28"
print("Day difference:", day_difference(date1, date2))


# ==================================================================================== #

# from datetime import datetime

# def day_thedifference(tarix1, tarix2):
#     tarix1 = datetime.strptime(tarix1, "%Y-%m-%d")
#     tarix2 = datetime.strptime(tarix2, "%Y-%m-%d")

#     difference = abs((tarix2 - tarix1).days)
#     return difference


# tarix1 = "2023-05-10"
# tarix2 = "2023-06-15"
# print({day_thedifference(tarix1, tarix2)})


# # ==================================================================================== #


# y = int(input("ili daxil edin"))
# m = int(input("ayı daxil edin"))
# d = int(input("günü daxil edin"))

# a = (y*365)+(m*30)+(d)

# y2 = int(input("ili daxil edin"))
# m2 = int(input("ayı daxil edin"))
# d2 = int(input("günü daxil edin"))


# b = (y2*365)+(m*30)+(d)
# print(a-b)
