from pydantic import BaseModel

class JSONResponseMessage(BaseModel):
    message: str