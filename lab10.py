import string
import random

# 1) 
def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for i in range(size))

# 2) 
def pw_chk(pwd):
    if len(pwd) == 8:
        print('low : ', end = '') 
    elif len(pwd) == 12: 
        print('middle : ', end = '') 
    else: 
        print('high : ', end = '')
    
    print(pwd)

while True:
    # Get input
    input_string = input('Guess a level password between low - middle - high. Type "exit" to exit the Gen. Pass:')
    if input_string.lower() == 'exit':
        print('See you next time!')
        break
    # Check the input value
    try:
        if input_string not in ['low', 'middle', 'high']:
            print('Your level is outrange.')
            continue
    except:
        print('Input error.')
        continue
    # Compare
    if input_string == 'low':
        pwd = pw_gen(8)
    elif input_string == 'middle':
        pwd = pw_gen(12)
    else:
        pwd = pw_gen(16)

    pw_chk(pwd)