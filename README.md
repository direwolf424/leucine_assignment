# README #

This README would normally document whatever steps are necessary to get your application up and running.
We are using sqlite3 as a database for now to store data.

### Dependencies ###

* Python 3.x


### Virtual Environment Setup ###

1. Setup virtualenv : "virtualenv -p python3 venv"
2. Activate virtualenv : "source venv/bin/activate"
3. Install Required Dependicies : "pip install -r requirements.txt"

### To Run Server ###
1. Go to leucine_assignment directory.(you will see manage.py present)
2. To run server : "python manage.py runserver 0.0.0.0:8000 --settings=tutorial.settings"


### API Documentation ###

1. To Upload a new document

        type: POST
        url: http://localhost:8000/quickstart/document/
        parameters: document_upload,name
        
2. To Fetch documents

        type: GET
        url: http://localhost:8000/quickstart/document/

3. To Rename documents
       
        type: PUT
        url: http://localhost:8000/quickstart/document/
        parameters: new_name,id
        
3. To Delete documents
       
        type: DELETE
        url: http://localhost:8000/quickstart/document/
        parameters: id

