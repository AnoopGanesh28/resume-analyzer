# app/core/schemas.py
from pydantic import BaseModel
from typing import List, Dict


class ResumeRequest(BaseModel):
    resume_path: str
    jd_path: str
    skills_db: List[str]


class ScoreResponse(BaseModel):
    skill_score: float
    semantic_score: float
    matched_skills: List[str]
