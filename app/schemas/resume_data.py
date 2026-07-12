from pydantic import BaseModel, EmailStr
from typing import List, Optional


class Experience(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    duration: Optional[str] = None


class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    year: Optional[str] = None


class Project(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = []


class ResumeData(BaseModel):

    name: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    summary: Optional[str] = None

    skills: List[str] = []

    certifications: List[str] = []

    experience: List[Experience] = []

    education: List[Education] = []

    projects: List[Project] = []
