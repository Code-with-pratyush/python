#check weather a nuber is paindrome or not
def palindrome(num):
    rev_num  = 0
    while num > 0:
        rem = num %10
        rev_num =  rev_num *10 + rem
        num  = num //10
    return rev_num

num  = int(input("Enter a number: "))
temp = num
res = palindrome(num)
if temp == res:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
# count the number of repeated letters in number
#converting the number into string
str_number = str(num)
for digit in range(len(str_number)):
    if str_number.count(str(digit)) != 0:
        print('Number of count of', digit, 'is:', str_number.count(str(digit)))
