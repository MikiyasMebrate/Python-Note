a=2
if (a > 0):
    print('A is a Positive number')
elif a < 0:
    print('A is a Negative number')
else: 
    print('A is Zero')

    #Short Hand
#code if condition else code
print('A is a Positive Number') if a > 0 else print('A is a negative number')


dic = {
    'first_name': 'Mikiyas',
    'last_name': 'Mebrate',
    'age':22,
    'skill': ['Java','Python','JavaScript','HTML','React'],
    'married' : False
}

if ('skill' in dic.keys() and 'Python' in dic.get('skill')):
    print(dic.get('skill'))

if('skill' in dic.keys()):
    if('JavaScript' in dic.get('skill') and 'Java' in dic.get('skill')  ):
        print('Front End Developer')



if(dic['married'] is False):
    print("Fullname: "+" "+dic['first_name'] + " "+ dic['last_name'] )