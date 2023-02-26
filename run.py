# Output welcome message
def welcome_message():
    '''
    Display the welcome logo and message
    '''
    print('''
    
    # # #   ####  #    #   #### #     ####  #    # #    # ##### #####
    #     # #   #  # #    #   # #     #   # ##   # ##   # #     #   #
    #     # #####   #     ####  #     ##### # #  # # #  # ##### ####
    #     # #   #   #     #     #     #   # #  # # #  # # #     # #
    # # #   #   #   #     #     ##### #   # #   ## #   ## ##### #  ##

    ''')

    print('Welcome to the Day Planer!')
    print('This program will help you to plan your day.')


print()


# Inputs

# Input name
def input_name():
    '''
    Collect the user name. And return it.
    '''
    name = input('Please enter your name: ')
    print('Hello ' + name + '!')
    
    return name

# Input age
def input_age():
    '''
    Collect the user age. And return it.
    '''
    age = input('Please enter your age: ')
    print('You are ' + age + ' years old!')
    
    return age

# Input sex
def input_sex():
    '''
    Collect the user sex. And return it.
    '''
    sex = input('Please enter your sex: ')
    print('You are ' + sex + '!')

    return sex

# Input height

def input_height():
    '''
    Collect the user height. And return it.
    '''
    height = input('Please enter your height: ')
    print('You are ' + height + ' cm!')
    
    return height

# Input weight

def input_weight():
    '''
    Collect the user weight. And return it.
    '''
    weight = input('Please enter your weight: ')
    print('You are ' + weight + ' kg!')
    
    return weight

# Input Goals

def input_goals():
    '''
    Collect the user goals. And return it.
    '''
    while True:
    goals = input('Please enter your goals: ')
    if goals == 'lose weight' or goals == 'gain weight' or goals == 'stay fit':
        print('Your goals are ' + goals + '!')
        break
    
    return goals

# Main function

def main():
    '''
    Run all the functions.
    '''
    welcome_message()

    name = input_name()
    age = input_age()
    sex = input_sex()
    height = input_height()
    weight = input_weight()

    goals = input_goals()
main()
