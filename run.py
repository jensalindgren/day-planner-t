# Colorama is used to color the text in the terminal
from colorama import Fore, Back, Style

# Input color
i_color = Fore.LIGHTGREEN_EX
# Error color
e_color = Back.RED
# Info Color
d_color = Fore.LIGHTYELLOW_EX
# Reset to normal
reset_all = Style.RESET_ALL
# Welcome message
b_color = Fore.BLUE

# Output welcome message


def welcome_message():
    '''
    Display the welcome logo and message
    '''
    print(Style.BRIGHT + Fore.BLUE + '''
      # # #   ####  #    #   #### #     ####  #    # #    # ##### #####
      #     # #   #  # #    #   # #     #   # ##   # ##   # #     #   #
      #     # #####   #     ####  #     ##### # #  # # #  # ##### ####
      #     # #   #   #     #     #     #   # #  # # #  # # #     # #
      # # #   #   #   #     #     ##### #   # #   ## #   ## ##### #  ##
    ''')

    print(Style.BRIGHT + d_color + '''
                       Welcome to the Day Planner!
                       ''' + reset_all)


print()


# Input name


def input_name():
    '''
    Collect the user name. And return it.
    '''
    while True:
        name = input(i_color + '''
                       Enter your name in letters:''' + reset_all)
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
        age = input(i_color + '''
                       Please enter your age:''' + reset_all)
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
    sex = input(i_color + '''
                       Are you a "male" or "female":''' + reset_all)
    while sex not in ["male", "female"]:
        print(e_color + '''
                       Invalid sex''' + reset_all)
        sex = input(i_color + '''
                       Please enter your sex:''' + reset_all)
    return sex

# Input height


def input_height():
    '''
    Collect the user height. And return it.
    '''
    while True:
        height = input(i_color + '''
                       Enter your height in cm:''' + reset_all)
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
        weight = input(i_color + '''
                       Enter your weight in kg:''' + reset_all)
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
        goals = input(i_color + '''
                       Enter your goals for the day:
                       1. Lose weight with cardio:
                       2. Gain weight with weight-training:
                       3. Maintain weight with weight-training:
                       ''' + reset_all)
        if goals == '1':
            while True:
                goal_level = input(i_color + '''
                       Please enter your level:
                       1. Beginner
                       2. Intermediate
                       3. Advanced
                       ''' + reset_all)
                if goal_level == '1':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Beginner training program and goals!
                       ''')
                    print('''
                       Level: Beginner

                       Cardio: 30-40 minutes interval training
                       5 minutes light running warmup
                       3 times a 800m interval.
                       2 minutes rest between each interval.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 2000 calories
                       Protein intake for the whole day: 160g
                       Carbohydrate intake for the whole day: 190g
                       Fat intake for the whole day: 80g
                       ''')
                    restart_program()

                elif goal_level == '2':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Intermediate training program and goals!
                       ''')
                    print('''
                       Level: Intermediate

                       Cardio: 60-70 minutes interval training
                       10 minutes light running warmup
                       3 times a 200m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 400m interval.
                       1 minute rest in between.
                       Followed by 2 times 800m interval. 2 minutes rest.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 1800 calories
                       Protein intake for the whole day: 180g
                       Carbohydrate intake for the whole day: 170g
                       Fat intake for the whole day: 60g
                       ''')
                    restart_program()

                elif goal_level == '3':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Advanced training program and goals!''')
                    print('''
                       Level: Advanced

                       Cardio: 60-70 minutes interval training
                       10 minutes light running warmup
                       3 times a 400m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 800m interval.
                       1 minute rest in between.
                       Followed by 4 times 200m interval. 2 minutes rest.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 1600 calories
                       Protein intake for the whole day: 200g
                       Carbohydrate intake for the whole day: 150g
                       Fat intake for the whole day: 40g
                        ''')
                    restart_program()

        elif goals == '2':
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       You want to gain weight-training!''')
            while True:
                goal_level = input(i_color + '''
                       Please enter your level:
                       1. Beginner
                       2. Intermediate
                       3. Advanced
                       ''' + reset_all)
                if goal_level == '1':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Beginner training program and goals!''')
                    print('''
                       Level: Beginner

                       Cardio: 30-40 minutes interval training
                       5 minutes light running warmup
                       3 times a 800m interval.
                       2 minutes rest between each interval.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 2800 calories
                       Protein intake for the whole day: 160g
                       Carbohydrate intake for the whole day: 250g
                       Fat intake for the whole day: 80g
                       ''')
                    restart_program()

                elif goal_level == '2':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Intermediate training program and goals!''')
                    print('''
                       Level: Intermediate

                       Cardio: 60-70 minutes interval training
                       10 minutes light running warmup
                       3 times a 200m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 400m interval.
                       1 minute rest in between.
                       Followed by 2 times 800m interval. 2 minutes rest.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 3200 calories
                       Protein intake for the whole day: 180g
                       Carbohydrate intake for the whole day: 320g
                       Fat intake for the whole day: 100g
                       ''')
                    restart_program()

                elif goal_level == '3':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Advanced training program and goals!''')
                    print('''
                       Level: Advanced

                       Cardio: 60-70 minutes interval training
                       10 minutes light running warmup
                       3 times a 400m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 800m interval.
                       1 minute rest in between.
                       Followed by 4 times 200m interval. 2 minutes rest.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 3500 calories
                       Protein intake for the whole day: 200g
                       Carbohydrate intake for the whole day: 350g
                       Fat intake for the whole day: 120g
                       ''')
                    restart_program()

        elif goals == '3':
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       You want to maintain your weight-training!''')
            while True:
                goal_level = input(i_color + '''
                       Please enter your level:
                       1. Beginner
                       2. Intermediate
                       3. Advanced
                       ''' + reset_all)
                if goal_level == '1':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Beginner training program and goals!''')
                    print('''
                       Level: Beginner

                       Cardio: 30-40 minutes interval training
                       5 minutes light running warmup
                       3 times a 800m interval.
                       2 minutes rest between each interval.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 2200 calories
                       Protein intake for the whole day: 160g
                       Carbohydrate intake for the whole day: 190g
                       Fat intake for the whole day: 80g
                       ''')
                    restart_program()

                elif goal_level == '2':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Intermediate training program and goals!''')
                    print('''
                       Level: Intermediate

                       Cardio: 60-70 minutes interval training.
                       10 minutes light running warmup
                       3 times a 200m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 400m interval.
                       1 minute rest in between.
                       Followed by 2 times 800m interval. 2 minutes rest.
                       Afterwards 5 minutes cooldown with
                       5 minutes stretching.

                       Calorie intake for the whole day: 2500 calories
                       Protein intake for the whole day: 180g
                       Carbohydrate intake for the whole day: 220g
                       Fat intake for the whole day: 100g
                       ''')
                    restart_program()

                elif goal_level == '3':
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Advanced training program and goals!''')
                    print('''
                       Level: Advanced

                       Cardio : 60-70 minutes interval training
                       10 minutes light running warmup
                       3 times a 400m interval.
                       2 minutes rest between each interval.
                       Afterwards followed by 2 times 800m interval.
                       1 minute rest in between.
                       Followed by 4 times 200m interval.
                       ''')
                    restart_program()
        else:
            print(e_color + '''
                       Please enter a valid number!''' + reset_all)
            continue

# Instructions


def inst():
    '''
    Help the user to use the application
    '''
    while True:
        instructions = input(i_color + '''
                       Here Are your options:
                       Type "start" "info" or "exit"
                       ''' + reset_all)
        if instructions.lower() == 'start':
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Lets start!''')
            return instructions
        elif instructions.lower() == 'info':
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Welcome to the fitness application!
                       This application will help you to
                       create a training program and
                       a meal plan based on your goals.
                       You will be asked to enter your
                       name, age, weight, height and
                       your goals.
                       The application will then create
                       a training program and a meal plan
                       for you.

                       You can choose between 3 different goals:
                       1. Weight loss
                       2. Weight gain
                       3. Maintain weight
                       You can also choose between 3 different levels:
                       1. Beginner
                       2. Intermediate
                       3. Advanced
                       ''' + reset_all)
            inst()
            return instructions
        elif instructions.lower() == 'exit':
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Goodbye!''')
            exit()

# Restart program


def restart_program():
    '''
    Allow the user to run the application
    once again or exit
    '''
    run_again = input(i_color + '''
                       Do you want to run the program again type:
                       "yes", "exit" or "menu".
                       ''' + reset_all)
    if run_again.lower() == 'yes':
        input_goals()
    elif run_again.lower() == 'exit':
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       Goodbye!''')
        exit()
    elif run_again.lower() == 'menu':
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
                       To the menu!''')
        inst()


# Validate name


def validate_name(name):
    '''
    Checks if the name is valid.
    And display error massage.
    '''
    try:
        if len(name) == 0:
            raise ValueError(e_color + '''
                       Enter a name in letters!''')
        elif name.isdigit():
            raise ValueError(e_color + '''
                       Enter a name in letters!''')
    except ValueError:
        print(e_color + '''
                       Enter a name in letters!''')
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
            raise ValueError(e_color + '''
                       Enter a valid age between 1 and 120!''' + reset_all)
    except ValueError:
        print(e_color + '''
                       Enter a valid age between 1 and 120!''' + reset_all)
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
            raise ValueError(e_color + '''
                       Enter a height between 100cm - 250cm!''' + reset_all)
    except ValueError:
        print(e_color + '''
                       Enter a height between 100cm - 250cm!''' + reset_all)
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
            raise ValueError(e_color + '''
                       Enter a weight between 40kg and 200kg!''' + reset_all)
    except ValueError:
        print(e_color + '''
                       Enter a weight between 40kg and 200kg!''' + reset_all)
        return False
    return True

# Display the results


# Main function


def main():
    '''
    Run all the functions.
    '''
    welcome_message()
    while True:

        inst()

        input_name()

        input_age()

        input_height()

        input_weight()

        input_sex()

        input_goals()


main()
