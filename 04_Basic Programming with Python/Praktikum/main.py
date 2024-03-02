def my_function():
    print("Hello my Function")

def my_function_with_params(username, greeting):
    # simbol %s artinya setelah kata Hello akan menerima sebuah data dengan type data str
    print("Hello, %s, From my Function! I wish you %s" %(username, greeting)) 

#nilai kembalian
def sum_two_numbers(a, b):
    return a + b    


# Call Function
my_function()
my_function_with_params("Alta", "Data Engineer")
x = sum_two_numbers(100, 200)
print(x)            #pemanggilan 1
print(sum_two_numbers(100, 200)) #pemanggilan 2