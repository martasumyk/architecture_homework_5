# architecture_homework_5

This homework consists of 3 FastAPI microservices:  client_service, business logic service, and database service. Each service runs through a HTTP request.

All the dependencies are in the requirements.txt, so to intall run:

pip install -r requirements.txt

Also, the .env file is ready.

To start each service:

uvicorn db_service:db_app --host 0.0.0.0 --port 8001 --reload

uvicorn business_service:business_app --host 0.0.0.0 --port 8002 --reload

uvicorn client_service:client_app --host 0.0.0.0 --port 8003 --reload
