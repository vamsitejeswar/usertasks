DJANGO REST API – USER & TASK MANAGEMENT
======================================

PROJECT OVERVIEW
----------------
This project is a Django REST API built using Django REST Framework (DRF) and PostgreSQL.
It provides APIs to manage Users and their Tasks.

The application supports:
- Creating and listing users
- Creating, listing, updating, and deleting tasks
- Filtering tasks by status and date
- Proper validation, error handling, and HTTP status codes

The project uses environment variables for database configuration

------------------------------------------------------------

TECH STACK
----------
- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Railway PostgreSQL (Cloud Database)
- pgAdmin
  
------------------------------------------------------------

SETUP INSTRUCTIONS
------------------

1. Clone Repository
   git clone <repository-url>
   cd usertasks

2. Create Virtual Environment
   python -m venv venv

   Activate:
   - Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Environment Variables
   Create a .env file in the root directory:

   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://user:password@host:5432/database

   Note:
   - DATABASE_URL uses Railway PostgreSQL public URL
   - SSL is required for Railway database connections

5. Run Migrations
   python manage.py makemigrations
   python manage.py migrate

6. Run Server
   python manage.py runserver

   Server URL:
   http://127.0.0.1:8000/

------------------------------------------------------------

MODELS IMPLEMENTED
------------------

User Model
- username (unique)
- email (unique)

Task Model
- title
- description
- status (Pending / In Progress / Completed)
- created_at (auto-generated)
- user (ForeignKey → User)

------------------------------------------------------------

API ENDPOINTS
-------------

USER APIs
---------
POST http://127.0.0.1:8000/app/users/
- Create a new user

GET http://127.0.0.1:8000/app/users/
- List all users

TASK APIs
---------
POST http://127.0.0.1:8000/app/tasks/
- Create a new task

GET http://127.0.0.1:8000/app/tasks/
- List all tasks

GET http://127.0.0.1:8000/app/tasks/{id}/
- Get task details

PUT http://127.0.0.1:8000/app/tasks/{id}/
- Update a task

DELETE http://127.0.0.1:8000/app/tasks/{id}/
- Delete a task

------------------------------------------------------------

FILTERING
-----------------

Filter tasks by status:
GET /tasks/?status=Completed

Combined filter:
GET /tasks/?status=Pending&date=2026-01-03

------------------------------------------------------------

API PAYLOADS (CHECKLIST)
-------------------------------

Create User
-----------
POST /users/

{
  "username": "vamsi",
  "email": "vamsi@example.com"
}

Expected Response:
- Status: 201 CREATED

------------------------------------------------------------

Create Task
-----------
POST /tasks/

{
  "title": "write an api",
  "description": "implement an api for the user tasks monitering",
  "status": "Pending",
  "user": 1
}

Expected Response:
- Status: 201 CREATED

------------------------------------------------------------

Get All Tasks
-------------
GET /tasks/

Expected Response:
- Status: 200 OK

------------------------------------------------------------

Update Task
-----------
PUT /tasks/1/

{
  "title": "Write API Updated",
  "description": "Updated description",
  "status": "Completed",
  "user": 1
}

Expected Response:
- Status: 200 OK

------------------------------------------------------------

Delete Task
-----------
DELETE /tasks/1/

Expected Response:
- Status: 204 NO CONTENT

------------------------------------------------------------

ERROR HANDLING & STATUS CODES
-----------------------------

- 201 CREATED        → Successful creation
- 200 OK             → Successful fetch
- 200 OK + message   → No data available
- 400 BAD REQUEST    → Validation errors
- 404 NOT FOUND      → Resource not found
- 204 NO CONTENT     → Successful delete

------------------------------------------------------------

ADMIN PANEL
-----------
- User and Task models are registered in Django Admin
- Accessible at:
  /admin/

Create superuser:
python manage.py createsuperuser
