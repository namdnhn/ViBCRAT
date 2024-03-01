from form import *
from fastapi.middleware.cors import CORSMiddleware
from relativeRisk import *
from absoluteRisk import *
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "sentry-trace", "baggage"],
)

@app.post("/form/")
async def post_form(data: Form):
    new_data = CheckedData(data)
    response = {"absolute risk": absoluteRiskWithoutT2(new_data), "absolute average": absoluteRiskAvgWithoutT2(new_data)}
    return JSONResponse(content=response)

@app.post("/form2")
async def post_form2(data: Form2):
    new_data = CheckedData2(data)
    response = {"absolute risk": absoluteRiskExact(new_data)}
    return JSONResponse(content=response)

@app.post("/vn")
async def post_vn(data: VietnamForm):
    new_data = VietnamData(data)
    response = {"absolute risk": absoluteRiskVietnam(new_data), "absolute average": absoluteAvgRiskVietnam(new_data)}
    return JSONResponse(content=response)