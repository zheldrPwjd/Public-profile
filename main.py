from fastapi import FastAPI
from pydantic import BaseModel
from service.mailer import sendMsg

from service.record_fire import record_fire_gps

app = FastAPI()

class FireInfo(BaseModel):
    serious: bool
    x_longitude: float
    y_latitude: float
    device_id: int 
    behave_kind: int 
    phoneNum: str



# 초기 화재 감지 => 문자 보내기.
@app.post("/fire") 
async def noticeFire(fireInfo: FireInfo):
    sendMsg(fireInfo)
    record_fire_gps(fireInfo)
    print(fireInfo.x_longitude, fireInfo.y_latitude)

# 화재 데이터 분석 결과 보여주기