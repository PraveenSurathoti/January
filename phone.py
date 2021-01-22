import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import tabulate

def number_scan(phone):
	numbers = phonenumbers.parse(phone)
	des = geocoder.description_for_numbers(number,"en")
	sup = carrier.name_for_number(number,"en")
	ifo = [["country","supplier"],[des,sup]]
	data = str(tabulate(info,headers="firstrow",tablefmt="github"))
	return data
	
if __name__== '__main__'
	number = input("Enter Number :")
	print(number_scan(number))
    