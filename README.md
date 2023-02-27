# Day Planner

## General Info

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

## User Stories

## Wireframes

### Flowchart
![Alt text](/assets/images/planner.png?raw=true "Flowchart")
## General Features

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

