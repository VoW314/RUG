#regular imports
import time
import datetime
import random
import pynput
import sys
import textwrap
import os
from os.path import join as pjoin
#cryptography
import cryptography
from cryptography.fernet import Fernet
#write to file
from sys import stdout

#code Actual
key = Fernet.generate_key()
print (key)

file = open('key.key', 'wb')
file.write(key)
file.close()

print("Your Name?")
uName = input()



a = 1
def loadBar():
    while (a >=10):
        bar = ["-"]
        a+1
        bar.append("-")
        os.system('cls' if os.name =='nt' else 'clear')
        #flush or something
        #WIP
#to make sure that the txt file exists and create one if it doesn't

os.system('cls' if os.name == 'nt' else 'clear')

hobby = [
    "playing the piano",
    "fishing",
    "cooking",
    "reading"
    #
    ]


gender = [
    "Male",
    "Female",
    "Apache Helicopter",
    "Other"
    ]
age1 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
age2 = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
age3 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]

ages = [age1, age2, age3]

c = ["Yes", "No"]#



company = [
    "Adobe",
    "Alphabet",
    "Berkshire Hathaway",
    "BioTech",
    "Cromwell's",
    "JP Morgan Chase",
    "Visa",
    "Nestle",
    "Samsung Electronics",
    "Royal Dutch Shell",
    "Nike",
    "Pfizer",
    "Wells Fargo",
    "Apple",
    "Cisco Systems",
    "Rukus",
    "Oracle",
    "Comcast",
    "BP",
    "Cheveron",
    "PayPal",
    "GE",
    "IBM",
    "AIRBUS",
    "Rio Tinto",
    "TDankGroup",
    "Ubisoft",
    "Bethesda",
    "Bungie",
    "Linde",
    "United Airlines",
    "Delta Airlines",
    "Emirates",
    "Naspers",
    "Medtronic",
    "3M"
    "Union Pacific",
    "Ping An Insurance Group",
    "Sinopec Group",
    "China National Petroleum",
    "Sasol",
    "MTN Group",
    "Eskom",
    "ShopRite Holdings",
    "ALFA",
    "Branco Bradesco",
    "Petrobras",
    "Toyota Motors",
    "TATA Motors",
    "Huwawei",
    "Verizon Communications",
    "Intel",
    "Mastercard",
    "Home Depot",
    "USPS",
    "FedEx",
    "Penguin Publishing",
    "DELL",
    "Yamaha",
    "Staples",
    ""
    "Dodge",
    "Elepaint",
    "Fortis Healthcare",
    "Google",
    "HeroMoto Corp",
    "Intel",
    "Jindal Steel and Power",
    "Kansas Oil",
    "Lithnic",
    "Microsoft",
    ""
    ]

job = [
    "Retail",
    "Doctor",
    "Investor",
    "IT",
    "Janitor",
    "Driver",
    "Secretary",
    "Engineer",
    "Mailroom Worker",
    "Data Entry Keyer",
    "Credit Authorizer",
    "Gardener",
    "Foreman",
    "Accountant",
    "Auditor",
    "Logistician",
    "Marketing Research",
    "Personal Finance Advisor",
    "Customer Support",
    "Employer",
    "Data Architect",
    "Budget Analysis",
    "Construction Worker",
    "Chemist",
    "Biologist",
    "Employer",
    "Cost Estimator",
    "Legal Analysist",
    "Legal Manager",
    "Cyber Specialist",
    "Security Guard",
    "Union Rep.",
    "Human Resources Rep.",
    "Human Resources Manager",
    "Gardener foreman",
    "Business Policy Enforcer",
    "Translator",
    "Website Designer"
    ]
bloodType = ["A+", "B+", "AB+", "A-", "B-", "AB-", "O+", "O-"]

#maidenName stuff 
lastN = [""]
def lastNames():
    if (country =="Chile" or "Argentina" or "Ecuador" or "Spain"):
        lastN = ["Alcón","García","Fernández","Rodríguez","Gonzalez","Diaz","Muñoz","Sanchez","Lopez","Zambrano"]
        
    elif(country =="India" or "Pakistan" or "Nepal" or "Bhutan" or "Bangladesh"):
        lastN =  ["Reddy", "Patel", "Devi", "Akvu", "Abidi", "Baqri","Farooqi", "Singh"]
        
    elif(country == "Belarus" or "Georgia" or "Kazakhstan" or "Russia"):
        lastN = ["Ivanov", "Oao", "Zao", "Zhuk", "Rup"]
        
    elif(country=="Germany" or "France"or "Italy" or "Papal State"):
        lastN = ["Muller", "Schmidth","Berger", "Chervolet", "Bisset", "Russo", "Ricci", "Colombo", "Esposito", "Abella"]
         
    else:
        lastN = "Whoop de doo"




country = [
    "Afghanistan",
    "Argentina",
    "Bahamas",
    "Bangladesh",
    "Belarus",
    "Belguim",
    "Bhutan",
    "Canada",
    "Chad",
    "Chile",
    "China",
    "Czechia",
    "Denmark",
    "Ecuador",
    "Estonia",
    "Finland",
    "France",
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
    "Nepal",
    "New Zealand",
    "Nigeria",
    "Oman",
    "Pakistan",
    "Papal State",
    "Qatar",
    "Russia",
    "Rwanda",
    "Samoa",
    "Saudi Arabia",
    "Serbia",
    "South Korea",
    "Spain",
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
    "Pacific Islander",
    "Caucasian",
    #
]
pet = ["dogs", "cats", "fish", "birds", "foxes"]#

lv = ["Alive", "Dead",]
lv1 = ["Alive", "Dead", "N/A"]
sibs = [0,1,2,3,4,5,6,7]


now = datetime.datetime.now()
print("How many people to create?")
x = int(input())
print("file has been edited. Open now")
top=print("ID CREATED AT",now, "by", uName)
print()
tad = 0

sys.stdout = open('People.txt' , "w")

def createID():
    top=print("ID CREATED AT",now, "by", uName)
    print('AGE:', random.choice(random.choice(ages)))
    #f.write('OCCUPATION:',random.choice(job)
    random.choice(random.choice(country))
    print('OCCUPATION:',random.choice(job))
    print('GENDER:',random.choice(gender))
    print('COMPANY:',random.choice(company))
    print('BT:',random.choice(bloodType))
    print('COUNTRY:',random.choice(country))
    #lastNames()
    print('RACE:',random.choice(race))
    print('MOTHERS MAIDEN NAME:',(lastNames()))
    print("")

    print("FAMILY")
    print('FATHER:',random.choice(lv))
    print('MOTHER:',random.choice(lv))
    print('SPOUSE:',random.choice(lv1))
    print('SIBLINGS:',random.choice(sibs))
    print('PETS:',random.choice(sibs),random.choice(pet))

    print("")
    print("INTERESTS")
    info= print("HOBBY:",random.choice(hobby))
    info=("HOBBY:",random.choice(hobby))
    print("_____________________________")
    print()

count = 1
while (count <=x):
    count = count + 1
    createID()

sys.stdout.close()


#notes
'''
    rework Maiden Name code

    organize code better(eh...)

    find a better purpose for the fernet

'''
