from fastapi import FastAPI
from pydantic import BaseModel
from workers.worker import run_company
app = FastAPI()
class GoalIn(BaseModel):
    goal:str
@app.post("/run_company")
async def run_ai_company(data: GoalIn):
    run_company.delay(data.goal)
    return {"status":"running","goal":data.goal}
