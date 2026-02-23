from fastapi import FastAPI
from sqlalchemy import create_engine,text
from fastapi.middleware.cors import CORSMiddleware

# 1. Database Connection URL
# Format: mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL="mysql+pymysql://root:mysecretpassword@localhost:3307/weather_db"

# 2. Create the SQLAlchemy Engine
# echo=True prints the generated SQL behind the scenes to your terminal for debugging
# True-> SQLAlchemy will log all the SQL statements it executes, which can be helpful for debugging and understanding how your code interacts with the database.
# False-> SQLAlchemy will not log any SQL statements, which can help reduce noise in your logs and improve performance in production environments.
engine=create_engine(DATABASE_URL,echo=True)

# 3. Create fastApi 
app=FastAPI(title="Daily Weather Logger API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# 4. A simple endpoint to make sure the server is awake
@app.get("/")
def read_root():
    return {"message":"Welcome to the Weather Logger API"}


# 5. An endpoint to test the database connection and fetch our dummy row
@app.get("/logs")
def get_weather_logs():
    with engine.connect() as connection:
        result=connection.execute(text("Select * from weather_logs"))
        logs=[]
        for row in result.mappings():
            logs.append(dict(row)) #this will be key value pair (row) and then we convert this to dict and append to list (logs) 

        return {"status":"success","data":logs} # its like status sucess and data is inside the logs somewhat like json format