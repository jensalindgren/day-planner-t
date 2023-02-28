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


# Inputs for all the data

# Input name

def input_name():
    '''
    Collect the user name. And return it.
    '''
    while True:
        name = input('Please enter your name in letters: ')
        if validate_name(name):
            return name
        else:
            continue

# Input age


def input_age():
    '''
    collect the user age. And return it.
    '''
    while True:
        age = input('Please enter your age in numbers: ')
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
    '''
    while True:
        height = input('Please enter your height in cm: ')
        if validate_height(height):
            return int(height)
        else:
            continue

# Input weight


def input_weight():
    '''
    Collect the user weight. And return it.
    '''
    while True:
        weight = input('Please enter your height in kg: ')
        if validate_weight(weight):
            return int(weight)
        else:
            continue


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
            continue
        if goals == '1':
            while True:
                goal_level = input('Please enter your goal level:' +
                                   '1. Beginner'
                                   '2. Intermediate'
                                   '3. Advanced')
                if goal_level == '1':
                    print('Beginner program and Goals!')
                    
                    
                    goal_data = {
                        'goal_level': 'Beginner',
                    }
                    return goal_data
            
        elif goals == '2':
            print('You want to gain weight!')
            break
        elif goals == '3':
            print('You want to maintain your weight!')
            break
        continue

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


# Validation for the inputs

# Validate name


def validate_name(name):
    '''
    Checks if the name is valid.
    And display error massage.
    '''
    try:
        if len(name) == 0:
            raise ValueError('Please enter a valid name!')
    except ValueError:
        print('Please enter a valid name!')
        return False

    return True


# Validate age


def validate_age(age):
    '''
    Checks if the age valid.
    And display error massage.
    '''
    try:
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError('Please enter a valid age between 1 and 120!')
    except ValueError:
        print('Please enter a valid age between 1 and 120!')
        return False
    return True

# Validate height


def validate_height(height):
    '''
    Checks if the height is valid.
    And display error massage.
    '''
    try:
        height = int(height)
        if height < 100 or height > 250:
            raise ValueError('Please enter a valid' +
                             'height between 100cm and 250cm!')
    except ValueError:
        print('Please enter a valid height between 100cm and 250cm!')
        return False
    return True

# Validate weight


def validate_weight(weight):
    '''
    Checks if the weight is valid.
    And display error massage.
    '''
    try:
        weight = int(weight)
        if weight < 40 or weight > 200:
            raise ValueError('Please enter a valid' +
                             'weight between 40kg and 200kg!')
    except ValueError:
        print('Please enter a valid weight between 40kg and 200kg!')
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