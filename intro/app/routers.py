from fastapi import APIRouter, Path, Query, Body
from asyncio import gather
from app.functions.converters import sync_converter, async_converter
from app.models.schemas import ConverterRequest, ConverterResponse

router = APIRouter()

@router.get('/converter-sync/{from_currency}')
def convert_sync(from_currency: str = Path(max_length=3, min_length=3), 
                 to_currencies: str = Query(default='BRL,EUR', max_length=3, min_length=3), 
                 price: float = Query(default=1.0,gt=0)):
    to_currencies = to_currencies.split(',') #to_currencies=USD,EUR,GPB

    results: list[float] = list()

    for currency in to_currencies:
        result = sync_converter(from_currency=from_currency, to_currency=currency, price=price)
        results.append(result)

    return results

@router.get('/converter-async/{from_currency}')
async def convert_async(from_currency: str = Path(max_length=3, min_length=3), 
                        to_currencies: str = Query(default='BRL,EUR', max_length=3, min_length=3), 
                        price: float = Query(default=1.0,gt=0)):
    to_currencies = to_currencies.split(',')

    coroutines = []

    for currency in to_currencies:
       coroutine = async_converter(from_currency=from_currency, to_currency=currency, price=price)
       coroutines.append(coroutine)

    result = await gather(*coroutines)
    return result

@router.post('/converter-async/{from_currency}', response_model=ConverterResponse)
async def convert_async(from_currency: str = Path(max_length=3, min_length=3), 
                        converter_request: ConverterRequest = Body(default={ "price": 1.0, "to_currencies": ['BRL'] })) -> ConverterResponse:
    
    to_currencies = converter_request.to_currencies
    price=converter_request.price

    coroutines = []

    for currency in to_currencies:
       coroutine = async_converter(from_currency=from_currency, to_currency=currency, price=price)
       coroutines.append(coroutine)

    result = await gather(*coroutines)
    return ConverterResponse(data=result)