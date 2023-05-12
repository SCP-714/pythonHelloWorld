name = input('Please tell me your name!')

if len(name) >= 20:
    print('Your Name is Too Long! Your name may not be longer than 20 letters!')
elif len(name) <= 2:

    print('Your Name is Too Short! Your name may not be shorter than 2 letters!')
else:
    print('Your Name is Awesome!')