# ⛱️ Family Day Out Planner
This poject is our final project for Holberton School. It is a simple web application that can be used to search a location on a specific date and will return a list of events at that location with futher details, like a map and weather information.

## 🌳 Environment:
This project has been completed using python3 (3.8.5) Will add more technologies as we work on them

## ⚙️ Installation

### Clone the repo locally using this command
```
gh repo clone https://github.com/Matthew-brinkmann/Family_day_out_planner
```
### build Docker Image:
```
docker image build -t family_day_out_server .
```
### Run Docker Image:
```
docker run -p 5000:5000 -d family_day_out_server
```
## 🛂 Testing:
All files, classes and functions can be tested with unit tests.

**Interactive mode:** 
```
python3 -m unittest discover tests
```


## 📁 File descriptions:
- models: contains all Python Scripting
- tests: contains unit tests for python scripts
- web_static: contains front end files

## 🐛 Bugs
No known bugs at this time.
## ✍🏽 Authors
- [Yuan Fang](https://github.com/yuan-fang-228)
- [Jacqueline Lu](https://github.com/Jql11)
- [Matthew Brinkmann](https://github.com/Matthew-brinkmann)
