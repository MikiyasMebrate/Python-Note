def seconda_largest(li):
    first_largest = li[0]
    second_largest = ""
    for i in li:
        if(i > first_largest):
            second_largest = first_largest
            first_largest = i

    print(first_largest)
    print(second_largest)




lstc = [2,3,5,676,4,3,7,8,500,700]       
seconda_largest(lstc)