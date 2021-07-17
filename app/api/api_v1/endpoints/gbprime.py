import time
import requests
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.models.gbprime import GbprimeBody
from app.gservice import gservice

router = APIRouter()

@router.get("/gen-gblinkpayment/{account_code}")
async def gen_gblinkpayment(
        account_code: str,
        name: str = '',
        campaign: str = 'LowCode101',
        email: str = '',
        mobile: str = '',
        address: str = '',
        amt: int = 1
):
    token, selected_setting = gservice.read_config_sheet(account_code, campaign)
    req_obj = GbprimeBody(
        token=token,
        amount=int(selected_setting['Price']) * amt,
        referenceNo=int(time.time()),
        backgroundUrl=selected_setting['Webhook'],
        detail=selected_setting['Description'],
        customerName=name
    )

    if email != '':
        req_obj.customerEmail = email

    if mobile != '':
        req_obj.customerTelephone = mobile

    if selected_setting.Delivery == 'Yes':
        if address != '':
            req_obj.customerAddress = address
        else:
            del req_obj.customerAddress

    res = requests.post('https://api.gbprimepay.com/gbp/gateway/link', json=req_obj.dict())
    return RedirectResponse(res.json()['gbLinkUrl'])
