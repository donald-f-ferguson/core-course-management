from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Section(BaseModel):
    callno: int
    dept_code: str
    course_no: str
    section_no: str
    semester: str
    year: str


class Model(BaseModel):
    uni: str
    sections: List[Section]