# # While loop and for loop

# #1 While loop
# #Syntax  while condition 
#        # code

# count=0
# while count < 5:
#     print(count)
#     count=count+1
# else:
#     print("False part: ",count)  #If the code is false


# #Break statement 
# count = 0
# while count < 5:
#     print(count)
#     count=count+1
#     if count==3:
#         break

# #Continue
# count = 0
# while count < 5:
#     count=count+1
#     if count==2:
#         continue
#     print("Countinue ",count)
         


# #For loop
# #Syntax
# # for itrator in 1st
#    #code


# numbers = [7,4,3,4,5,6]
# #for each loop
# for i in numbers:
#     print(i, end=" ")

# print("\n")
# #loop with strings
# language = 'python'
# for i in language:
#     print(i, end="   ")


# print('\n')
# #using range
# for i in range(len(language)):
#     print(language[i], end="   ")


# #itrerat in dictionaries 
# person = {
#     'first_name': 'Mikiyas',
#     'last_name' : 'Mebrate',
#     'age' : 22,
#     'country' : 'Ethiopia',
#     'is_marred' : False,
#     'skills' : ['JavaScript', 'Python', 'Java', 'C++'],
#     'address': {
#          'street': 'Signal',
#         'zipcode': '09222'
#     }
# }
# print('\n')

# for i in person:  #Only print the keys
#     print(i)


# print('\n\n\n')
# for key,value in person.items():
#     print(key, value)


# #loop in sets
# it_compnies = {'facebook', 'google', 'Microsoft', 'Apple', 'IDM', 'Oracle'}
# for com in it_compnies:
#     print(com, end="  ")


# #Range Function
# #The range(start, end, increment) 
# #default starts from 0 and increment in 1
# print('\n\n\n')
# lis = list(range(11))
# print(lis)

# lis = list(range(1,10,2))
# print(lis)

# #nasted loop
# for key in person.keys():
#     if(key == 'skills'):
#         for skill in person['skills']:
#             print(skill, end="  ")


#Exercise
#print 0 to 10
for i in range(11):
    print(i, end=" ")

print('\n')
count = 0
while count < 11:
    print(count, end=" ")
    count = count+1

print('\n')
#print 10 to 0
for i in range(10,-1,-1):
    print(i ,end=" ")

print('\n')
count=10
while count >= 0:
    print(count, end=" ")
    count=count-1

print('\n')
#Shapes
hash = '#'
for i in range(7):
    print(hash)
    hash = hash +'#'

print('\n')
for i in range(8):
    for j in range(8):
        print('#',end=" ")
    print()


#Pattern 
print('\n')
for first in range(11):
    print(first, " x ", first, " = ", first*first)


#print lists
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for l in lst:
    print(l, end=" ")
print('\n')

sum = 0
for i in range(101):
    sum = sum + i

print('The sum of all numbers is: ' ,sum)

print('\n')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]


for country in range(len(countries)):
    if 'land'  in countries[country]:
        print(countries[country])


#Reverse
