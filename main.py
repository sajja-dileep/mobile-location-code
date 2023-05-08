"""use the pip comand in terminal and type pip install phonenumbers """
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter your phone number ")
phone=phonenumbers.parse(number)
timee=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(timee)
print(car)
print(reg)