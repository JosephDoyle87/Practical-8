number=int(input('Enter your number: '))
count = 0
import sys

if number >= 0 and number <= 20:
    print('This number is greater than 0 and less than 20')
    count+=1
        
elif number >= 20 and number <= 40:
     print('This number is greater than 20 and less than 40')
     count+=1
        
elif number >= 40 and number <= 60:
     print('This number is greater than 40 and less than 60')
     count+=1
           
elif number >= 60 and number <= 80:
     print('This number is greater than 60 and less than 80')
     count+=1
        
elif number >= 80 and number <= 100:
     print('This number is greater than 80 and less than 100')
     count+=1
        
elif number >= 100:
     print('This number is greater than 100')
     count+=1

number=int(input('Enter your number: '))

else:
    print('This is not a positive number')
    sys.exit()

    
