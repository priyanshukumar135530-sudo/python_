def outer_function(num):

    def inner_function(n):
        return n * n   

    result = inner_function(num)
    return result


number = int(input("Enter a number: "))
print("Square is:", outer_function(number))
