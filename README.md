# fastapi-crud-api
FastAPI app with basic CRUD (GET, POST, DELETE) operations

# FastAPI CRUD
This is a simple project that shows how to build an API using **FastAPI** and how to test it using **Pytest**. It also uses **GitHub Actions** to automatically test the code whenever something is pushed to GitHub.

---

---  
It also shows how to use **Thunder Client** or **Postman** to test endpoints locally.(For checking API response)

## What This Project Teaches

- How to create a FastAPI project
- How to write test cases using Pytest
- How to automate testing using GitHub Actions (CI/CD)
- How to check test results in GitHub

## Project Structure

build-api/
├── main.py # Main API code (FastAPI)
├── test_main.py # Test cases for the API
├── requirements.txt # All required libraries
└── .github/
└── workflows/
└── test.yml # GitHub Actions workflow file

# Features

- GET request with query and path parameters
- POST request with JSON body
- DELETE request for removing items
- Easy to run and test locally

## How to Run This Project Locally

Clone the Repository
git clone https://github.com/your-username/fastapi-crud-api.git
cd fastapi-crud-api

Create a virtual environment by writing this command:
python -m venv venv

Activate the environment
For Windows:
venv\Scripts\activate

For macOS/Linux:
source venv/bin/activate

Install Required Packages
pip install -r requirements.txt

Run the FastAPI app:
uvicorn apitest:app --reload

![image](https://github.com/user-attachments/assets/86d86fc5-2708-4234-9ed2-c2ddce9c029a)


# Testing the API
You can test all endpoints using:
Thunder Client (VS Code Extension)
Postman
For this project I have user Thunder Client:

**For GET:**
METHOD: GET: http://127.0.0.1:8000/items/1?q=pen

![image](https://github.com/user-attachments/assets/20e94722-71ed-4b1b-9f6a-71756916d1c1)


**FOR POST:**
METHOD: POST:http://127.0.0.1:8000/items/1
Go to the Body tab:
Select JSON
Paste your JSON:
And check the response:
Click Send and check the response on Thunder client

![image](https://github.com/user-attachments/assets/1c2d7041-143a-4c50-91c3-0e2583fd3de0)

**FOR DELETE:**
METHOD: DELETE: http://127.0.0.1:8000/items/1

![image](https://github.com/user-attachments/assets/8390377d-4d7f-4ff0-ab3a-16db4edde659)

**How to Run Tests Locally**
To check if the API is working correctly, run the test cases using:
pytest test_main.py

![image](https://github.com/user-attachments/assets/f0c1fcd5-3e4d-442f-8666-5e6d60b397eb)

If everything is working, all tests will pass.

GitHub Actions: Automated Testing
Every time you push code to GitHub, this project automatically runs all the test cases using GitHub Actions.

**What It Does**
Installs Python
Installs all required packages
Runs the test file test_main.py
Shows result (pass ✅ or fail ❌)

**Where to See Test Results**
Go to your GitHub repo
Click the "Actions" tab at the top

![image](https://github.com/user-attachments/assets/37e6d98b-8de9-4d8d-871a-eecded80df16)


You'll see a list of runs (green = passed ✅, red = failed ❌)

Click any run to see detailed logs

![image](https://github.com/user-attachments/assets/be2f018a-2f83-45ac-85fb-78dbcf0c47dd)

![image](https://github.com/user-attachments/assets/33ee6ef8-d3e4-43eb-a701-397eb5781653)

**Final Notes**
All tests are passing 
GitHub Actions is working correctly 
The project is clean, understandable, and beginner-friendly 



