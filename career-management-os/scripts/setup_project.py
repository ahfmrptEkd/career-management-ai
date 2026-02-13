#!/usr/bin/env python3
"""
Initialize a new Career Management OS workspace.

Usage:
    python setup_project.py [project_path]

If no path is given, creates in current directory.
"""

import os
import sys
import shutil
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "templates"

DIRS = [
    "src",
    "instruction",
    "outcome/1-draft",
    "outcome/2-verify",
    "outcome/3-review",
    "outcome/4-refine",
]

TEMPLATE_MAP = {
    "templates/applicantinfo_template.md": "src/applicantinfo.md",
    "templates/jd_template.md": "src/jd.md",
    "templates/resume_workflow.md": "instruction/resume_workflow.md",
}


def init_project(target: Path):
    print(f"🚀 Initializing Career Management OS at: {target}")

    # Create directories
    for d in DIRS:
        (target / d).mkdir(parents=True, exist_ok=True)
        print(f"  📁 {d}/")

    # Copy templates
    for src_rel, dst_rel in TEMPLATE_MAP.items():
        src = SKILL_DIR / src_rel
        dst = target / dst_rel
        if not dst.exists() and src.exists():
            shutil.copy2(src, dst)
            print(f"  📄 {dst_rel}")
        elif dst.exists():
            print(f"  ⏭️  {dst_rel} (already exists, skipping)")

    print("\n✅ Done! Next steps:")
    print("  1. Fill in src/applicantinfo.md with your career data")
    print("  2. Paste the target JD into src/jd.md")
    print("  3. Run: /draft-resume")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    init_project(target)
