import phonenumbers  # we installed pip install phonenumbers
from phone2 import number  # phone2(another .py file)contains phone numbers

from phonenumbers import geocoder  # get country infromation
from phonenumbers import carrier  # carrier provides us the service provider number
# carrier another built-in-func


# number contains my ph no. from phone2 file/ # c-country/h-history
country_name = phonenumbers.parse(number[1])
region = (geocoder.description_for_number(country_name, "en"))
# OR DIERECT- print(geocoder.description_for_number(number, "en"))
print(region)

carrier = carrier.name_for_number(country_name, "en")
print(carrier)

# TO CHECK NUMBER VALID OR NOT
valid = phonenumbers.is_valid_number(country_name)
print(valid)
