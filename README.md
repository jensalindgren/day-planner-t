# Day Planner

## General Info

This is a simple day planner application that allows users to choose a training goal and choose the level of difficulty. The application will then generate a workout plan for the user. It will also give the user guidance on how to perform the exercises and how many reps and sets to do. The application will also give the user a nutrition plan based on their goal and level of difficulty.

![Alt text](/assets/images/one.png?raw=true "One")

Here is the link to the deployed application: [Day Planner](https://day-planner.herokuapp.com/)

## Table of Contents

- [Day Planner](#day-planner)
  - [General Info](#general-info)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Color Scheme](#color-scheme)
  - [Wireframes](#wireframes)
    - [Flowchart](#flowchart)
  - [General Features](#general-features)
  - [Testing](#testing)
    - [Code validation](#code-validation)
    - [Manual Testing](#manual-testing)
  - [Final Result](#final-result)
  - [Deployment](#deployment)
  - [Features Left to Implement](#features-left-to-implement)
  - [Credits](#credits)

## Project Goals

- Create a simple day planner application that allows users to choose a training goal and choose the level of difficulty.
- The application will then generate a workout plan for the user.
- It will also give the user guidance on how to perform the exercises and how many reps and sets to do.
- The application will also give the user a nutrition plan based on their goal and level of difficulty.
- The application will allow individual users input.

## User Stories

- As a user, I want to be able to understand the purpose of the application.
- As a user you want to get a new workout plan every time you choose a new goal and level of difficulty.
- As a user, I want to be able to choose a training goal.
- As a user, I want to be able to choose the level of difficulty.
- As a user, I want to be able to see a workout plan based on my goal and level of difficulty.
- As a user, I want to be able to see a nutrition plan based on my goal and level of difficulty.
- As a user, I want to be able to see a list of exercises and their descriptions.
- As a user I want to be able to understand the instructions on how to perform the exercises.

## Color Scheme

Colorama was used to generate the color scheme. And make the terminal colorful.
In the terminal run: pip3 install colorama

- All the instructions are in green.
- All the user's input is in white.
- All the application's output is in yellow.
- All the errors are in red.
- Welcome message is in blue.
- And goodbye message is in yellow.

## Wireframes

### Flowchart

Flowchart was created in lucidchart.com
![Alt text](/assets/images/planner.png?raw=true "Flowchart")
## General Features

1 The user will input their name, age, sex, height and weight.
2 The user will choose a training goal.
2 The user will choose the level of difficulty.
3 The application will generate a workout plan based on the user's goal and level of difficulty.
4 The application will generate a nutrition plan based on the user's goal and level of difficulty.
5 The application has validation for all the user's input.
6 The application has a instructions section for all what the user needs to know about the application.

## Testing

### Code validation
- I used https://pep8ci.herokuapp.com/ to validate the code.

![Alt text](/assets/images/pep8.png?raw=true "Pep8")
### Manual Testing

I tested the application functions. And all the validations for the user's input.
All the different inputs to navigate the application.

- I tested the application manually to see if all validations works by following these steps:

![Alt text](/assets/images/validations/vali1.png?raw=true "Validation 1")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali2.png?raw=true "Validation 2")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali3.png?raw=true "Validation 3")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali4.png?raw=true "Validation 4")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali5.png?raw=true "Validation 5")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali6.png?raw=true "Validation 6")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali7.png?raw=true "Validation 7")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali8.png?raw=true "Validation 8")
- Valdiation test : Pass
![Alt text](/assets/images/validations/vali9.png?raw=true "Validation 9")
- Valdiation test : Pass

## Final Result

Here is the link to the deployed application: [Day Planner](https://day-planner.herokuapp.com/)

All the the workout plans and nutrition plans are created by myself.
For the estimation of the calories,carbs,proteins and fats is from my own experience working as a personal trainer and nutritionist.

Screenshots of the application deployed on Heroku:

![Alt text](/assets/images/one.png?raw=true "One")
![Alt text](/assets/images/two.png?raw=true "Two")
![Alt text](/assets/images/three.png?raw=true "Three")
![Alt text](/assets/images/four.png?raw=true "Four")

back to [top](#table-of-contents)
## Deployment

The application has been deployed using Heroku by following these steps:

Heroku was used to deploy the application.

1. Create the requirements.txt file and run: pip3 freeze > requirements.txt in the console.
2. Commit changes and push them to GitHub.
3. Go to the Heroku's website.
4. From the Heroku dashboard, click on "Create new app".
5. Enter the "App name" and "Choose a region" before clicking on "Create app".
6. Go to "Config Vars" under the "Settings" tab.
7. Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
8. Add the Config Var, KEY: PORT and VALUE: 8000.
9. Go to "Buildpacks" section and click "Add buildpack".
10. Select "python" and click "Save changes"
11. Add "nodejs" buildpack as well using the same process.
12. Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
13. Go to "Connect to GitHub" section and "Search" the repository to be deployed.
14. Click "Connect" next the repository name.
15. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

Here is the link to the deployed application: [Day Planner](https://day-planner.herokuapp.com/)

## Features Left to Implement

- Add a feature that allows users to choose the number of days they want to train.
- More exercises and nutrition plans.
- Tailor more the workout plans and nutrition plans to the user's inputs.
- Add more levels of difficulty.
- More training goals.
- Better design in comparison to the current design.
- Macros are calculated based on the user's inputs.

## Credits

I want to thank my mentor Marcel for his help and support.

I got the inspiration for this project from [Code Institute](https://github.com/josswe26/macro-calculator/tree/f3b008689f1ec2ee69833bbd41f679e36a9dad5e).

Feel free to use the code for your own projects.

[Back to Table of Contents](#table-of-contents)
