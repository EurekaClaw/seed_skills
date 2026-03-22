import logging
from pathlib import Path
from skill import SkillRecord, SkillMeta
import yaml
import frontmatter
import shutil

def upsert(skill: SkillRecord) -> None:
    """Write a skill to the skills directory and update the registry."""
    folder_path = Path(__file__).parent / skill.meta.name
    file_name = "SKILL.md"
    meta_dict = skill.meta.model_dump(mode="json")
    # Drop None values so they don't serialize as the string 'null'
    meta_dict = {k: v for k, v in meta_dict.items() if v is not None}
    frontmatter_block = yaml.dump(meta_dict, default_flow_style=False, allow_unicode=True)
    file_content = f"---\n{frontmatter_block}---\n\n{skill.content}"
    folder_path.mkdir(exist_ok=True)
    file_path = folder_path / file_name
    file_path.write_text(file_content, encoding="utf-8")
    logging.info(f"Upserted skill '{skill.meta.name}' to {file_path}")
    

def load_file(path) -> None:
    post = frontmatter.load(str(path))
    meta_dict = dict(post.metadata)
    meta = SkillMeta.model_validate(meta_dict)
    # if is_seed and seed_stats and meta.name in seed_stats:
    #     entry = seed_stats[meta.name]
    #     meta.usage_count = entry.get("usage_count", meta.usage_count)
    #     meta.success_rate = entry.get("success_rate", meta.success_rate)
    record = SkillRecord(meta=meta, content=post.content, file_path=str(path))
    return record


all_md_files = list(Path(__file__).parent.rglob("*.md"))
origin_dirs = [d for d in Path(__file__).parent.iterdir() if d.is_dir()]

all_records = []
for md_file in all_md_files:
    if md_file == Path(__file__).parent / "README.md":
        continue
    record = load_file(md_file)
    all_records.append(record)

for record in all_records:
    upsert(record)

for origin in origin_dirs:
    if origin == Path(__file__).parent / ".git":
        continue
    shutil.rmtree(origin)
    
