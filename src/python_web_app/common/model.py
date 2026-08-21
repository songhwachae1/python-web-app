from pydantic import BaseModel, ConfigDict

class SnakeModel(BaseModel):
    """This class is for converting a SQLAlchemy model to a Pydantic model"""
    model_config = ConfigDict(from_attributes=True, extra="allow")