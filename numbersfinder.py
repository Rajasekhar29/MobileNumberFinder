import phonenumbers as ph
# from . import text
from text import number
from phonenumbers import geocoder,carrier

#  showing the country of the number
ch_number = ph.parse(number,region='INDIA')
print(geocoder.description_for_number(ch_number,"en"))
# it shows the service number
service_number = ph.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))



