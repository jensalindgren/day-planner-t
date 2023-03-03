# Day Planner

## General Info

This is a simple day planner application that allows users to choose a training goal and choose the level of difficulty. The application will then generate a workout plan for the user. It will also give the user guidance on how to perform the exercises and how many reps and sets to do. The application will also give the user a nutrition plan based on their goal and level of difficulty.

## Table of Contents

- [Day Planner](#day-planner)
  - [General Info](#general-info)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
    - [Flowchart](#flowchart)
  - [General Features](#general-features)
    - [Index Page](#index-page)
  - [Testing](#testing)
    - [Code validation](#code-validation)
  - [Manual Testing](#manual-testing)
    - [Index](#index)
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

## Wireframes

### Flowchart
![Alt text](/assets/images/planner.png?raw=true "Flowchart")
## General Features

- The application is easy to use and navigate.
- The application has instructions on how to use it.
- The application has a list of exercises and their descriptions.
- The application has a workout plan based on the user's goal and level of difficulty.
- The application has a nutrition plan based on the user's goal and level of difficulty.
- The application has validation for all the user's input.
### Index Page

## Testing

### Code validation

## Manual Testing

### Index

## Final Result

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

## Credits

