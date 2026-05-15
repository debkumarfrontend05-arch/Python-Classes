# a = 1;

# while a<=30:
#     print(a);
#     a = a + 1;


# a = int(input("Please enter a number "));
# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10;
#     a = a //10
# if copy == rev:
#     print('Palimdrom Number')
# else:
#     print('Not Palimdrom Number')


import random;

num = random.randint(1,100);
trid = 0;
print(num);

while True:
    guess = int(input('Please guess a number between 1-10 '));
    if num == guess:
        trid+=1;
        print(f'You are Right and tried {trid} times');
        break;
    elif num < guess:
        print('Go a little lower');
        trid+=1;
    elif num > guess:
        print('Go a little higher');
        trid+=1;
    else:
        trid +=1;
        print('You are wrong');