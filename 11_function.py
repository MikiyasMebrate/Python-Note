#def key word
#Syntax def function_name():     parameter
    #   codes

#Syntax def function_name(paramer):   Parameter
    #   codes


def greetings (name):
    msg = name + ', Welcome to python for Everyone! '
    return msg


print(greetings('Mike'))


def sum_all_numbers(*nums):
    total =0
    for i in nums:
        total = total+i
    return total

print(sum_all_numbers(2,3,4,5))