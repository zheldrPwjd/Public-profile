from fastapi import FastAPI
from pydantic import BaseModel
from mailer import sendMsg

app = FastAPI()

class FireInfo(BaseModel):
    serious: bool
    x_longitude: float
    y_latitude: float
    phoneNum: str

# 초기 화재 감지 => 문자 보내기.
@app.post("/fire") 
async def noticeFire(fireInfo: FireInfo):
    sendMsg(fireInfo)
    print(fireInfo.x_longitude, fireInfo.y_latitude)

# 화재 데이터 분석 결과 보여주기