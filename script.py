
from random import randint
from time   import sleep

def line(par=60):
        print('-'*par)

vetor = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','10','!','@','#','$','%','¨','&','*','(',')','?','/']
# for a in range(1, 11):
#     print(f"\'{a}\'", end=',')

line()
print(f'{"Welcome to our System":^60}')
line()

print('How many characteres would you like on your password?')

while True:
    num = str(input("How many? "))
    if(num.isalnum == True):
        pass
    else:
        while num.isalnum == False:
            num = str(input("How many? "))
            if(num.isalnum == True):
                break
    break

print('Generating your password in ', end='')
for c in range(1, 4):
    sleep(1)
    print(c, end='')
    for c in range(1, 4):
        sleep(0.5)
        print('.', end='')
    sleep(1.3)
    print(' ', end='')
print()

sleep(1)
print('Your password is: \"', end='')
for c in range(0, num):
    print(vetor[randint(0, len(vetor))], end='')
print('\"')



def leaving():
    print('Thanks for use our system', end='')
    for c in range(0, 3):
            sleep(1.7)
            print('.', end='')
    print()

line()
leaving()
