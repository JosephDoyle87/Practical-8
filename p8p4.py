number = int(input('enter a positive integer: '))
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
while number >= 0:
    if number>0:
        if number == 0:
            print ('this number is equal to 0')
            count1 += 1
        if number > 0 and number <20:
            print ('this number is greater than 0 and less than or equal to 20')
            count2 += 1
        if number > 20 and number<= 40:
            print ('this number is greater than 20 and less than or equal to 40')
            count3 += 1
        if number > 40 and number<= 60:
            print ('this number is greater than 40 and less than or equal to 60')
            count4 += 1
        if number > 60 and number<= 80:
            print ('this number is greater than 60 and less than or equal to 80')
            count5 += 1
        if number > 80 and number<= 100:
            print ('this number is greater than 80 and less than or equal to 100')
            count6 += 1
        if number > 100:
             print ('this number is greater than 100')
             count7 += 1
                
    else:
        print ('number cannot be less than zero')
    
    number = int(input('Enter a number: '))
    
