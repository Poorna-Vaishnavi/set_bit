num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
def set_bits_and_convert(num1,num2):
    num = (1 << num1) | (1 << num2)
    return num
result = set_bits_and_convert(num1, num2)
print("Output:", result)