import os
import pytest
import pathlib

REPO_ROOT = pathlib.Path(__file__).parent.parent / "seedskills"

# Directories at repo root that are NOT skill folders
EXCLUDED_DIRS = {"tests", ".git", ".github", "__pycache__"}


def get_skill_dirs():
    return [
        d for d in os.listdir(REPO_ROOT)
        if os.path.isdir(os.path.join(REPO_ROOT, d))
        and d not in EXCLUDED_DIRS
        and not d.startswith(".")
    ]


@pytest.mark.parametrize("skill_dir", get_skill_dirs())
def test_skill_has_skill_md(skill_dir):
    skill_md_path = os.path.join(REPO_ROOT, skill_dir, "SKILL.md")
    assert os.path.isfile(skill_md_path), (
        f"Missing SKILL.md in directory: '{skill_dir}'"
    )