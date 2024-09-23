from __future__ import annotations

from pydantic import BaseModel


class Model(BaseModel):
    callno: int
    dept_code: str
    course_no: str
    section_no: str
    semester: str
    year: str
    role: str