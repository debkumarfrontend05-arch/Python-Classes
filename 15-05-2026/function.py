def Hello(name):
    print(f'Hello {name},How are you',);

Hello('Debkumar');


def sum(a,b):
    print(f'Sum of {a} and {b} is {a+b}');
sum(10,25);

def profile(name,age):
    print(f'You name is {name} and your age is {age}');

profile(age=26,name='Debkumar');


def palimdrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev += str[i]
    if rev == str:
        print('Palimdrome');
    else:
        print('Not a palimdrome number');

palimdrome('mam')
