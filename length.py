name = input('Please tell me your name!')

if len(name) >= 20:
    print('Your Name is Too Long!')
elif len(name) <= 2:
    print('Your Name is Too Short!')
else:
    print('Your Name is Awesome!')