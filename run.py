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

    print('Welcome to the Day Planner!')
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
    collect the user age. And return it.
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
        if goals == '1':
            print('You want to lose weight!')
            break
        elif goals == '2':
            print('You want to gain weight!')
            break
        elif goals == '3':
            print('You want to maintain your weight!')
            break
        else:
            print('Please enter a valid number 1-3!')

# Main function


def main():
    '''
    Run all the functions.
    '''
    welcome_message()
    input_name()
    input_age()
    input_height()
    input_weight()
    input_goals()


main()