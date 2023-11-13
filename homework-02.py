# Darryl Laiu
# 2 Nov 2023
# Homework 2

user_year = input("When is your birth year?: \n")
user_year = int(user_year)
# print(user_year)

#10. If someone says they were born in the future, ask them for their year of birth again. Assume they'll do it right the second time.
if (user_year > 2023):
    user_year = input("Try again. Which year were you born in? \n")
    user_year = int(user_year)

#1. How old are you
year = 2023
# print(year)
age = year - user_year
print("You are " + str(age) + " years old.")

#2. how many times does your heart beat in a year?
heartbeats_in_a_year = 35000000
user_heartbeats = age * heartbeats_in_a_year
print("Your heart beat about " + str(user_heartbeats) + " times.")

#3. In that time, how many times a blue whale's heart has beaten.
whale_heartbeats_a_year = 17344800
user_whale_hearbeats = user_year * whale_heartbeats_a_year
print("A blue whale's heart has beaten " + str(user_whale_hearbeats) + " times.")

#4. In that time, how many times a rabbit's heart has beaten. If the answer to rabbit heartbeats is more than a billion, say "XXX billion" instead of the very long raw number
rabbit_heart_beat = 94608000
user_rabbit_heartbeat = rabbit_heart_beat * age
# print(user_rabbit_heartbeat)
user_rabbit_heartbeat = round(user_rabbit_heartbeat/1000000000, 1)
print("A rabbit's heart beaten " + str(user_rabbit_heartbeat) + " billion times")

# 5. There are several ways to calculate and format/display numbers 
# in Python – string addition, f-strings, commas, etc etc etc. Redo one of the above questions 
# above with another technique and briefly explain the pros and cons of each approach.

print("You are %s years old." % age)

#6. Whether they are the same age as you, older or younger
#If older or younger, how many years difference
#If they were born in an even or odd year

admin_age = 28
if age == admin_age:
    print("We're the same age.")
elif age > admin_age: 
    print("You're older.")
elif age < admin_age:
    print("I'm older.")

if (user_year % 2) == 1:
    print("You were born in an odd year.")
else: 
    print("You were born in an even year.")

# 7. How many times there has been a president from the Democratic Party 
# in office since they were born (1980 onward, and each president only counts once)
if (user_year < 1993):
    print("There has only been 1 Democrat President since you were born.")
elif (user_year < 2009):
    print("There have been 2 Democrat Presidents since you were born.")
elif (user_year < 2021):
    print("There have been 3 Democrat Presidents since you were born.")
else:
    print("There have been 4 Democrat Presidents since you were born.")

# 8. Which US President was in office when they were born (1980 onward)
if(user_year == 1980):
    print("Jimmy Carter was President.")
elif(user_year < 1989):
    print("Ronald Reagan was President.")
elif(user_year < 1993):
    print("George Bush was President.")
elif(user_year < 2001):
    print("Bill Clinton was President.")
elif(user_year < 2009):
    print("George W. Bush was President.")
elif(user_year < 2016):
    print("Barack Obama was President")
elif(user_year < 2021):
    print("Donald Trump was President")
elif(user_year < 2025):
    print("Joe Biden was President")

# 9.Can you think of another approach to #7 and/or #8 that you could have tried? Why is yours better? 
# If you could not get #7/#8 to work, use this question to explain what you were trying to do.

presidents = {
    1980: "Jimmy Carter",
    1989: "Ronald Reagan",    
    1993: "George Bush",    
    2001: "Bill Clinton",   
    2009: "George W. Bush",
    2017: "Barack Obama",
    2021: "Donald Trump",
    2025: "Joe Biden"
}

for key, value in presidents.items():
    if (user_year < key):
        print("%s was President." % value)
        break
