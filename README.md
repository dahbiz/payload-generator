This a python program that **generates** more than 100 payload!

This is for educational purposes! 


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




You can add as many payload as you want to the **payload.txt** file. Just respect the way the txt file is written, and the host variable is called **mhost**.
