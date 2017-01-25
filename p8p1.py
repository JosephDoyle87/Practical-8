number = int(input('Enter a number: '))


while number >= 0:
    if number %2 == 0:
        print ('number is divisible by 2')
    if number %3 == 0:
        print ('number is divisible by 3')
    if number %5 == 0:
        print ('number is divisible by 5')
    if number %7 == 0:
        print ('number is divisible by 7')
    number = int(input('Enter a number: '))
    
print (number)
    
    
