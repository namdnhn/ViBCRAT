# ViBCRAT - Vietnam Breast Cancer Assessment Tool
This project is a tool estimating personal risk and predicting the probability of developing breast cancer in the future for Vietnamese women.

# Build with

In this project, the following technologies were utilized:

* Front-end:
  - Vue.js
  - Tailwind CSS
 
* Back-end:
  - Python
  - FastAPI
 
# Installation Guide

## Step 1: Clone the Project

```bash
git clone https://github.com/namdnhn/ViBCRAT
cd ViBCRAT
```

## Step 2: Install Dependencies
### Install dependencies for the back-end
Prerequisites: Python must be installed on your machine. Our version: 3.10.11

Instructions:

Navigate to the app folder in the project, create a .env file with the content of the .env.example file and modify the information to match your machine.

- Create a virtual environment: ```python -m venv env```
- Activate the virtual environment:
    + Windows: ```env\Scripts\activate```
    + MacOS and Linux: ```source env/bin/activate```
- Install the dependencies for the virtual environment: ```pip install -r requirements.txt```

### Install dependencies for the front-end
- From the root directory
- ```bash
  cd vue-project
  npm install
  ```

## Step 3: Run the project

```bash
* Run the back-end
cd backend
uvicorn main:app --reload

* Open a new terminal window

* Run the front-end
cd vue-project
npm run dev
```
