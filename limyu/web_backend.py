import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8012",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
async def testApi():
    import inc_file.db_conn as dbcon
    dbcls = dbcon.db_con()
    dbcon = dbcls.dbconnection()
    cursor = dbcon.cursor()
    cursor.execute("SELECT no, name, birthday, tel, DATE_FORMAT(create_date, '%Y%m%d') FROM yulim_test")
    rows = cursor.fetchall()
    djson = rows
    '''
    returnarray = []

    dataDict = {}
    dataDict["no"] = 1
    dataDict["name"] = "yulim"
    dataDict["tel"] = "01012345154"
    dataDict["birthday"] = "761001"

    returnarray.append(dataDict)

    dataDict = {}
    dataDict["no"] = 2
    dataDict["name"] = "seounghapark"
    dataDict["tel"] = "01025487745"
    dataDict["birthday"] = "810101"

    returnarray.append(dataDict)
    print(json.dumps(dataDict))
    '''

    return djson







