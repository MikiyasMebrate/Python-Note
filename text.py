import sys

def seconda_largest(li):
    first_largest = sys.maxsize * -1
    second_largest = sys.maxsize * -1
    for i in li:
        if(i > first_largest):
            second_largest = first_largest
            first_largest = i
        if(i < first_largest and i > second_largest):
            second_largest = i

    print(first_largest)
    print(second_largest)




lstc = [900,3,5,676,4,800,7,8,1000,700]       
seconda_largest(lstc)