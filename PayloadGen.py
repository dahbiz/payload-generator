host = input('FREESITE: ')

print('\n ######################## ALL PAYLOADS ########################## \n')
payloads = open('payloads.txt', 'r') 

index = 0

for payload in payloads:
    if payload != ' \n':
        index += 1
        print(f'\n \n ****************** $$ PAYLOAD {index} $$ ******************** \n \n')

        print(payload.replace("mhost", host))
        
print('\n ######################## THE END ########################## \n')

