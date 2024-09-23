from __future__ import annotations

from pydantic import BaseModel
from typing import Union, List

from links import Link


class UserInfo(BaseModel):
    last_name: str
    first_name: str
    middle_name: Union[str, None]
    email: str
    uni: str
    contact_phone: str


class UserInfoRsp(BaseModel):
    data: UserInfo
    links: List[Link]


