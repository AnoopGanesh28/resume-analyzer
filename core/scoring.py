import logging
from typing import Dict, List

from core.models import EmbeddingModel
from core.parser import extract_skills

logger = logging.getLogger(__name__)


def compute_scores(resume_text: str, jd_text: str, skills_db: List[str]) -> Dict[str, float]:
    """
    Compute different matching scores between resume and job description.

    Args:
        resume_text (str): Text extracted from resume
        jd_text (str): Text extracted from job description
        skills_db (List[str]): Database of skills

    Returns:
        Dict[str, float]: Scores for skill match and semantic similarity
    """
    model = EmbeddingModel()

    # Skill-based matching
    resume_skills = set(extract_skills(resume_text, skills_db))
    jd_skills = set(extract_skills(jd_text, skills_db))
    overlap = resume_skills.intersection(jd_skills)
    skill_score = round(len(overlap) / len(jd_skills), 2) if jd_skills else 0.0

    # Semantic similarity
    semantic_score = model.similarity(resume_text, jd_text)

    return {
        "skill_score": skill_score,
        "semantic_score": semantic_score,
        "matched_skills": list(overlap),
    }
