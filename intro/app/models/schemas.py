from pydantic import BaseModel, Field, validator
from typing import List

class ConverterRequest(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @validator('to_currencies')
    def validate_to_currencies(cls, to_currencies):
        for curr in to_currencies:
            if len(curr) != 3:
                raise ValueError(f'Currency must have 3 characteres: {curr}')
        return to_currencies
    

class ConverterResponse(BaseModel):
    data: List[dict]