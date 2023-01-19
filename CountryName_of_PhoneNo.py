import phonenumbers
from phonenumbers import geocoder
print("Number of phone numbers") 
length_of_list=int(input())
list_of_numbers=[]
if length_of_list:
    print("Enter your number in the following format")
    print("countrycode xxxxxxxxxx")

    for i in range(1,length_of_list+1):
        print("Enter the phone number "+str(i))
        number=input()
        list_of_numbers.append(number)
    for number in list_of_numbers:
        ch_number=phonenumbers.parse(number, "CH")
        print(number,end=" : ")
        country=geocoder.description_for_number(ch_number, "en")
        if len(country):
            print(country)
        else:
            print("INVALID INPUT")
else:
    print("NO INPUT")
