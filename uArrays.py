import time
import random
import pynput
import os
from time import sleep
#currently a 1/1187856384 chance of getting two of the same people
gender = [
    "Male",
    "Female",
    "Apache Helicopter",
    "Other"
    ]
age1 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
age2 = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
age3 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]

c = ["Yes", "No"]#

company = [
    "Adobe",
    "BioTech",
    "Cromwell's",
    "Dodge",
    "Elepaint",
    "Fortis Healthcare",
    "Google",
    "HeroMoto Corp",
    "Intel",
    "Jindal Steel and Power",
    "Kansas Oil",
    "Lithnic",
    "Microsoft"
    ]
job = [
    "Retail",
    "Doctor",
    "Investor",
    "IT",
    "Janitor",
    "Driver",
    "Blue Collar Worker",
    "Construction Worker",
    "Chemist",
    "Biologist",
    "Employer"
    ]
bloodType = ["A+", "B+", "AB+", "A-", "B-", "AB-", "O+", "O-"]

country = [
    "Afghanistan",
    "Argentina",
    "Bahamas",
    "Belarus",
    "Belguim",
    "Canada",
    "Chad",
    "Chile",
    "China",
    "Czechia",
    "Denmark",
    "Ecuador",
    "Estonia",
    "Finland",
    "Fracne",
    "Georgia",
    "Germany",
    "Guyana",
    "Hungary",
    "Iceland",
    "India",
    "Iraq",
    "Italy",
    "Iran",
    "Jamaica",
    "Kazakhstan",
    "Laos",
    "Lebanon",
    "Madagascar",
    "Maldives",
    "Mexico",
    "Mongolia",
    "New Zealand",
    "Nigeria",
    "Oman",
    "Pakistan",
    "Qatar",
    "Russia",
    "Rwanda",
    "Samoa",
    "Saudi Arabia",
    "Serbia",
    "South Korea",
    "Turkey",
    "Thailand",
    "Ukraine",
    "UAE",
    "UK",
    "USA",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia"
    ]
race = [
    "Arab",
    "Asian",
    "Sub-Saharan",
    "Latino",
    "Hispanic",
    "Pacific Islander",
    "Caucasian",
    #
]
pet = ["dogs", "cats", "fish", "birds", "30MM HEDP"]#

lv = ["Alive", "Dead",]
lv1 = ["Alive", "Dead", "N/A"]
sibs = [0,1,2,3,4,5,6,7]
print("How many people to create?")
x = int(input())
print("young, mid-life, or old?")
ageNum = input("")
os.system('cls' if os.name == 'nt' else 'clear')


os.system('cls' if os.name =='nt' else 'clear')
def createUser():
    if (ageNum=="young"):
        print("AGE:",random.choice(age1))
    elif(ageNum=="mid-life"):
        print("AGE:",random.choice(age2))
    elif(ageNum=="old"):
        print("AGE:",random.choice(age3))
    else:
        print("Age : 18")
    print('OCCUPATION:',random.choice(job))
    print('GENDER:',random.choice(gender))
    print('COMPANY:',random.choice(company))
    print('BT:',random.choice(bloodType))
    print('COUNTRY:',random.choice(country))
    print('RACE:',random.choice(race))
    print()

    print("FAMILY")
    print("SIBLINGS:",random.choice())
    print('FATHER:',random.choice(lv))
    print('MOTHER:',random.choice(lv))
    print('SPOUSE:',random.choice(lv1))
    print('SIBLINGS:', random.choice(sibs))
    print('PETS:',random.choice(sibs),random.choice(pet))

    print("INTERESTS")


    print("_____________________________")

count = 1
while (count <=x):
    count = count + 1
    createUser()
