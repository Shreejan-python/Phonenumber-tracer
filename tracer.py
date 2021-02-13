import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone = input("Please give your country code : ")
service_provider = phonenumbers.parse(phone) 
print(carrier.name_for_number(service_provider, 'en')) 

phone_number = phonenumbers.parse(phone)  

print(geocoder.description_for_number(phone_number,  'en'))