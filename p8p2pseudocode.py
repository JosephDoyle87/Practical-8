#Prompt the user for a number
number = int(input('enter a positive integer: '))
#set vertical part of table to 0
i=0
while i <= number:
    #set horizontal part of table to 0
    j=0
    
    while j <=i:
        print (i multiplied by j,"line break",end=" ")
        #increment horizontal part of table by 1
        j +=1
    print()
    #increment vertical section of table by 1
    i += 1 
