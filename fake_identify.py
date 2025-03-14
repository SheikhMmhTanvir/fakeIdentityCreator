from numpy import random as rn
import numpy as np

first_names = [
    "Rakib", "Sabbir", "Nusrat", "Mehedi", "Tanjila",
    "Farhan", "Shakib", "Mahi", "Arif", "Jannat"
]

last_names = [
    "Rahman", "Hossain", "Islam", "Khan", "Ahmed",
    "Chowdhury", "Sarker", "Mia", "Hasan", "Uddin"
]

street_names = [
    "Motijheel Road", "Gulshan Avenue", "Banani Road",
    "Dhanmondi 27", "Baily Road", "Shahbagh Street",
    "Uttara Sector 4", "Mirpur 10", "Paltan Road",
    "Bashundhara Main Road"
]

fake_cities = [
    "Nabogram", "Sonarpara", "Chandrapur",
    "Nimtala", "Udaypur", "Shibganj",
    "Modhupur", "Aminbazar", "Kazipur", "Banshkhali"
]
states_name = [
    "Dhaka", "Chattogram", "Khulna", "Barishal",
    "Rajshahi", "Sylhet", "Rangpur", "Mymensingh"
]
x=int(input("How many fack identity need : "))
for info in range(x):
    street=rn.choice(street_names)
    city=rn.choice(fake_cities)
    state=rn.choice(states_name)

    # identity part
    fist = rn.choice(first_names)
    last = rn.choice(last_names)
    address=f'{state} St. {city}, {state}'
    phone = f'01{rn.randint(7, 8)}{rn.randint(100, 999)}{rn.randint(29033,58678)}'
    gmail=fist.lower()+last.lower()+'@gmail.com'

    print(f'{fist} {last}\n{phone}\n{address}\n{gmail}\n')