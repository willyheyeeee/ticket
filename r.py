Kevin=(30,24,37,24,28)
number=int(input('begin: '))
number2=int(input('end: '))
for i in range(number,number2):
    if(Kevin[i]>=25):
        print(f'round {i+1}: {Kevin[i]}')