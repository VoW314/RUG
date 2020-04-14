#regular imports
import time
import names
from random import *
import datetime
import random
import sys
import textwrap
import os
from os.path import join as pjoin
#cryptography

#write to file
from sys import stdout

#code Actual


'''
key = Fernet.generate_key()
print(key)
file = open('key.key', 'wb')
file.write(key)
file.close()
'''
print('WELCOME TO Random User Generator (RUG)')
time.sleep(1)




#
print("Your Name?")
uName = input()




os.system('cls' if os.name == 'nt' else 'clear')


mail = [
    "@gmail.com",
    "@yahoo.com"
    "@me.org",
    "@Outlook.com",
    "@aol.com",
    "@Bluebottle.com",
    "@Care2.com",
    "@LinuxMail.org",
    "@LitePost.com",
    "@Runbox.com",
    "@VFEmail.net"
    ]
#arrays
hobby = [
    "playing the piano",
    "fishing",
    "cooking",
    "reading",
    "making home videos",
    "playing the trumpet",
    "playing the vioin",
    "playing the drum",
    "walking the dogs",
    "babysitting",
    "volunteering",
    "charity work",
    "pet sitting",
    "no recorded hobbies",
    "gaming",
    "sleeping"
    ]

color = [
  "red",
  "blue",
  "green",
  "yellow",
  "black",
  "purple",
  "burgundy",
  "crimson",
  "royal blue",
  "white",
  "gray",
  "lime",
  "gold",
  "silver",
  "brown",
  "violet",
  "orange"
]


gender = [ #make smaller chance of getting the vehicles
    "Male",
    "Female",
    "Apache Helicopter",
    "A-10 Warthog",
    "Other"
    ]

traveled = False

def travel():
    tvl=randint(0,1)
    if (tvl==0):
        traveled=False
    elif(tvl==1):
        traveled=True
    if(traveled == True):
        print('RECENT VACATION TO:',random.choice(country))
    else:
        pass

sexuality = [
    "Straight",
    "Gay",
    "Other"
    ]

heliNames= [
    "Boeing AH-64 Apache",
    "WAH-64 Longbow Apache",
    "AH-64/D Apache"
    ]

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
    "Texas Instruments",
    "Tesla",
    "Nautica",
    "Macy's",
    "Belk",
    "Reebok",
    "Liberty",
    "Office Max",
    "Scholastic",
    "CNN",
    "Fox News",
    "MSNBC",
    "ABC",
    "Blaze News",
    "Epoch Times",
    "Washington Times",
    "Mayo Clinic",
    "Discover",
    "National Geographic",
    "Insignia",
    "Reynolds Wraps",
    "Clorox",
    "Oxi-clean",
    "Dodge",
    "Tortise Healthcare",
    "Elepaint",
    "Fortis Healthcare",
    "Google",
    "HeroMoto Corp",
    "Intel",
    "Jindal Steel and Power",
    "Kansas Oil",
    "Lithnic",
    "Microsoft",
    "Lenovo"
    ]

warNames = ['brrrrrrt', 'BRRRRRTT', 'COMMUNISM WAS NEVER AN OPTION']

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

heliThings = [
    "STILL MORE NATIVE AMERICAN THAN SEN. ELIZABETH WARREN",
    "NOTHING'S MORE POWERFUL THAN A CHILD'S WISHES ... EXCEPT AN APACHE HELICOPTER",
    "Supply deliver",
    "Helicopter right's activist",
    "RTRTRTRTRTRTRTRTRTR"
    ]

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

pet = ["dogs", "cats", "fish", "birds", "foxes"]#

lv = ["Alive", "Dead",]
lv1 = ["Alive", "Dead", "N/A"]

sibs = [0,1,2,3,4,5,6,7]

yan1 = randint(100, 999)
yan2 = randint(100,999)
yan3 = randint(1000,9999)



#last names
'''
lastN = [""]
def lastNames():
    if (country =="Chile" or "Argentina" or "Ecuador" or "Spain"):
        lastN = ["Alcón","García","Fernández","Rodríguez","Gonzalez","Diaz","Muñoz","Sanchez","Lopez","Zambrano"]
        random.choice(lastN)

    elif(country =="India" or "Pakistan" or "Nepal" or "Bhutan" or "Bangladesh"):
        lastN =  ["Reddy", "Patel", "Devi", "Akvu", "Abidi", "Baqri","Farooqi", "Singh"]
        random.choice(lastN)

    elif(country == "Belarus" or "Georgia" or "Kazakhstan" or "Russia"):
        lastN = ["Ivanov", "Oao", "Zao", "Zhuk", "Rup"]
        random.choice(lastN)

    elif(country=="Germany" or "France"or "Italy" or "Papal State"):
        lastN = ["Muller", "Schmidth","Berger", "Chervolet", "Bisset", "Russo", "Ricci", "Colombo", "Esposito", "Abella"]
        random.choice(lastN)

    else:
        pass
'''
ideology = [
    "absolutism",
    "anarchism",
    "autocracy",
    "capatilsim",
    "communism",
    "democracy",
    "republic",
    "dictatorship",
    "facism",
    "egalitarianism",
    "Maxism",
    "Maoism",
    "Stalinst",
    "Leninsm",
    "socialism",
    "theocracy",
    "Trotskyism"
    ]



now = datetime.datetime.now()
print("How many people to create?")
x = int(input())
print("file has been edited. Open now")
top=print("ID CREATED AT",now, "by", uName)
print()

sys.stdout = open('People.txt' , "w")
top=print("ID CREATED AT",now, "by", uName)
print('________________')


def createID():
    print()
    random.choice(country)
    ages = randint(18,79)
    print('AGE:', ages)
    random.choice(random.choice(country))
    gendy=random.choice(gender)
    print('GENDER:',gendy)
    if (gendy=="Apache Helicopter"):
        jargoon = random.choice(heliThings)
    else:
        jargoon = random.choice(job)
    
    print('OCCUPATION:',jargoon)

    #name stuff
    
    if(gendy=='Male'):
        jargon = names.get_full_name(gender='male')
    elif(gendy=='Female'):
        jargon = names.get_full_name(gender='female')
    elif(gendy=='Other'):
        jargon = names.get_full_name()
    elif(gendy=='Apache Helicopter'):
        jargon = random.choice(heliNames)
    elif(gendy=='A-10 Warthog'):
        jargon = random.choice(warNames)
    
    print('LEGAL NAME:',jargon)
    jargan = (jargon+random.choice(mail))
    print('E-MAIL:' , jargan)
    print('PHONE NUMBER:',yan1, yan2, yan3)

    print('COMPANY:',random.choice(company))
    print('BT:',random.choice(bloodType))
    print('COUNTRY:',random.choice(country))
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
    print("SEXULAITY:",random.choice(sexuality))
    print()
    
    print('OTHER')
    print('FAVORITE COLOR:', random.choice(color))
    travel()
    print('By latests comments their preferred ideology is:')
    print(random.choice(ideology))
    print("_____________________________")
    print()

count = 1
itt = 1
while (count <=x):
    print('#',itt)
    itt+=1
    count +=1
    createID()

itt -=1
print('IDs created #:',itt)
sys.stdout.close()


#notes
'''
    rework gender and names 

    organize code better(eh...)
    
    Use similar code for all the txt files:
    https://github.com/sbtnRey/Random-Animal-Generator/blob/master/randomAnimalGen.py
    making arrays in txt files will conserve space
    
    find a better purpose for the fernet

'''

