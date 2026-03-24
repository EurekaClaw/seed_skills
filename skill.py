from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field
import os
from pathlib import Path
import shutil


class SkillMeta(BaseModel):
    name: str
    version: str = "1.0"
    tags: list[str] = Field(default_factory=list)
    agent_roles: list[str] = Field(default_factory=list)   # AgentRole values
    pipeline_stages: list[str] = Field(default_factory=list)
    description: str = ""
    source: Literal["seed", "distilled", "manual"] = "seed"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    usage_count: int = 0
    success_rate: float | None = None


class SkillRecord(BaseModel):
    meta: SkillMeta
    content: str            # Full .md body after frontmatter
    file_path: str = ""     # Absolute path to .md file
    embedding: list[float] | None = None

    @property
    def full_markdown(self) -> str:
        return self.content


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    subdirs = [d.name for d in current_dir.iterdir() if d.is_dir()]
    for subdir in subdirs:
        if subdir.startswith("."):
            continue
        if subdir == "seedskills":
            continue
        skill_dir = current_dir / subdir
        shutil.move(str(skill_dir), str(current_dir /"skills" / subdir))
