# # #def key word
# # #Syntax def function_name():     parameter
# #     #   codes

# # #Syntax def function_name(paramer):   Parameter
# #     #   codes


# # def greetings (name):
# #     msg = name + ', Welcome to python for Everyone! '
# #     return msg


# # print(greetings('Mike'))


# # def sum_all_numbers(*nums):
# #     total =0
# #     for i in nums:
# #         total = total+i
# #     return total

# # print(sum_all_numbers(2,3,4,5))


# def add_list(lst:list)-> int: #Retun type is int
#     '''
#     This function return sum of lst
#     '''
#     sum = 0
#     for i in lst:
#         sum = sum + i
    
#     return sum



# lst = [1,2,3,5,8,6,4,6,8,5,3]
# print(add_list(lst))


# #lambda Expression 

# #lambda arr() : exp
# #greet = lambda arr() : exp
#    #greet()


#greet_user = lambda name: print('hey there, ' , name)

odd_eve = lambda num: print('Even') if num%2==0 else print ('Odd')


even_odd_n = lambda num : num+2 if(num%2==0) else num*2
lst = [1,2,4,7,4,3,6,9,5,4]
result = map(even_odd_n, lst)

#print(list(result))
stm = ['mikiyas', 'mebrate', 'ae', 'mmm', 'ouu']

def return_vowels(st):
    vowel = ['a','e','i','o','u']
    count = 0
    for i in st:
        if(i in vowel):
            count = count +1
    return  True if count > 2 else False 

print(list(filter(return_vowels, stm)))