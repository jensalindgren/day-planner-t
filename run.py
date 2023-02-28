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
    Also check if the name is valid.
    And display error massage.
    '''
    name = input('Please enter your name: ')
    try:
        name = str(name)
        if len(name) == 0:
            print('Please enter a valid name!')
            input_name()
    except ValueError:
        print('Please enter a valid name!')
        input_name()
    print('Hello ' + name + '!')
    return name

# Input age


def input_age():
    '''
    collect the user age. And return it.
    Also check if the age is valid.
    And display error massage.
    '''
    while True:
        age = input('Please enter your age: ')
        if validate_age(age):
            return int(age)
        else:
            continue


# Input sex


def input_sex():
    '''
    Collect the user sex. And return it.
    Also check if the sex is valid.
    And display error massage.
    '''
    sex = input('Please enter your sex: ')
    while sex not in ["male", "female"]:
        print("Invalid sex")
        sex = input('Please enter your sex: ')
    print('You are ' + sex + '!')

    return sex

# Input height


def input_height():
    '''
    Collect the user height. And return it.
    Also check if the height is valid.
    And display error massage.
    '''
    height = input('Please enter your height: ')
    try:
        height = int(height)
        if height < 130 or height > 230:
            print('Please enter a valid height!')
            input_height()
    except ValueError:
        print('Please enter a valid height!')
        input_height()
    print('You are ' + height + ' cm!')
    return height

# Input weight


def input_weight():
    '''
    Collect the user weight. And return it.
    Also check if the weight is valid.
    And display error massage.
    '''
    weight = input('Please enter your weight: ')
    try:
        weight = int(weight)
        if weight < 40 or weight > 200:
            print('Please enter a valid weight')
            input_weight()
    except ValueError:
        print('Please enter a valid weight')
        input_weight()
    print('You are ' + weight + ' kg!')
    return weight


# Input Goals


def input_goals():
    '''
    Collect the user goals. And return it.
    '''
    while True:
        goals = input('Please enter your goals:' +
                      '1. Lose weight'
                      '2. Gain weight'
                      '3. Maintain weight:')
        if input(goals) not in ['1', '2', '3']:
            print('Please enter a valid number 1-3!')
        elif goals == '1':
            print('You want to lose weight!')
            break
        elif goals == '2':
            print('You want to gain weight!')
            break
        elif goals == '3':
            print('You want to maintain your weight!')
            break
    return goals

# Restart program


def restart_program():
    '''
    Allow the user to run the application
    once again or exit
    '''
    run_again = input(''' Do you want to run the program again?
                      ''')
    if run_again.lower() == 'yes':
        main()
    else:
        print('Thank you for using the program!')
        exit()
    return run_again

# Validate age


def validate_age(age):
    try:
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError('Please enter a valid age between 1 and 120!')
    except ValueError:
        print('Please enter a valid age between 1 and 120!')
        return False
    return True


# Main function


def main():
    '''
    Run all the functions.
    '''
    while True:
        welcome_message()
        input_name()
        input_age()
        input_height()
        input_weight()
        input_goals()
        restart_program()
        if not restart_program():
            break


main()