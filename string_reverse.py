def string_reverse(input_string):
    reverse_string = input_string[::-1]
    return reverse_string
input_string = input("Enter a String")
print("users give this string")
print(input_string)
result = string_reverse(input_string)
print("users revrese string")
print(result)