# fastapi-crud-api
FastAPI app with basic CRUD (GET, POST, DELETE) operations

# FastAPI CRUD
This is a simple **FastAPI** project that demonstrates basic **CRUD operations** (GET, POST, DELETE) using `FastAPI`, `Pydantic`, and Python 3.  

It also shows how to use **Thunder Client** or **Postman** to test endpoints locally.

# Features

- GET request with query and path parameters
- POST request with JSON body
- DELETE request for removing items
- Easy to run and test locally

# Steps
Create a virtual environment by writing this command:
python -m venv venv

Activate the environment
For Windows:
venv\Scripts\activate

For macOS/Linux:
source venv/bin/activate

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
