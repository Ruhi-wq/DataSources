from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import data_aggr as dat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.route("/")
async def root():
    return {"message": "Hello World"}

@app.route("Get_Data/PMC")
async def PMC_Metadata():
    obj= dat.get_pubmedcen_ids("cancer",10)
    