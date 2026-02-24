from pydantic import BaseModel,Field
from typing import Literal

class Task(BaseModel):
    id:int= Field(gt=0)
    name:str=Field(min_length=3)
    description:str
    completed:bool= False
    priority:Literal['high','medium','low']