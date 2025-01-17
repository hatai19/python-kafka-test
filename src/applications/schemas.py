from pydantic import BaseModel

class ApplicationCreateSchema(BaseModel):
    user_name: str
    description: str

