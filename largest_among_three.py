def largest_number(num1,num2,num3):
    '''
    largest_number
    :param num1:
    :param num2:
    :param num3:
    :return:
    '''
    if (num1 >= num2) and (num1 >= num3):
       largest = num1
    elif (num2 >= num1) and (num2 >= num3):
       largest = num2
    else:
       largest = num3

    print("The largest number is", largest)

if __name__ == '__main__':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    largest_number(num1, num2, num3)