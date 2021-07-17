from typing import Optional
from pydantic import BaseModel


class GbprimeBody(BaseModel):
    token: str
    amount: float
    referenceNo: int
    payType: str = "F"
    cardUse: str = "Y"
    billUse: str = "N"
    qrUse: str = "Y"
    expire: int = 30
    deliveryMethod: str = "0"
    multipleUse: str = "N"
    wechatUse: str = "Y"
    responseUrl: str = ""
    backgroundUrl: str
    detail: str
    customerAddress: str = "-"
    customerName: str
    customerEmail: Optional[str]
    customerTelephone: Optional[str]
    customerAddress: str = "-"
