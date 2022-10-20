# ⛱️ Family Day Out Planner
This poject is our final project for Holberton School. It is a simple web application that can be used to search a location on a specific date and will return a list of events at that location with futher details, like a map and weather information.

## 🌳 Environment:
This project has been completed using python3 (3.8.5) Will add more technologies as we work on them

## ⚙️ Installation

### Clone the repo locally using this command
```
git clone https://github.com/Matthew-brinkmann/Family_day_out_planner
```
### Build and Run Docker Image:
```
cd family-day-out
npm install --save react-places-autocomplete
npm install react-datepicker --save
npm install —save moment
npm run build
cd ..
docker-compose up
```
The page can be viewed on localhost:5006
### Dependencies:
* docker
* docker-compose
* python-dotenv
* .env file in root directory containing:
```
EVENT_API_KEY=<API KEY>
WEATHER_API_KEY=<API KEY>
MYSQL_ROOT_USER=<SQL USERNAME>
MYSQL_ROOT_PASSWORD=<SQL PASSWORD>
SLACK_WEBHOOK=<WEBHOOK URL PROVIDED BY SLACK>
```
## 🛂 Testing:
All files, classes and functions can be tested with unit tests.

**Interactive mode:** 
```
RUN_UNITTEST=True python3 -m unittest discover tests
```


## 📁 File descriptions:
- api: contains the flask files, views and blueprints
- docker: contains all files required for docker configurations
- family-day-out: contains front end react application files
- models: contains all Python Scripting
- presentation: Contains the presentation for the project.
- tests: contains unit tests for python scripts


## 🐛 Bugs
No known bugs at this time.
## ✍🏽 Authors
- [Yuan Fang](https://github.com/yuan-fang-228)
- [Jacqueline Lu](https://github.com/Jql11)
- [Matthew Brinkmann](https://github.com/Matthew-brinkmann)
