#!/usr/bin/env python3
"""Lightweight structural checks for all local Agent Skills; not a behavior test."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('adaptive-autonomy', 'rapid-prototype', 'deep-engineering')


def validate(skill: str) -> list[str]:
    path = ROOT / skill / 'SKILL.md'
    errors = []
    if not path.is_file():
        return [f'{skill}: missing SKILL.md']
    source = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', source, re.DOTALL)
    if not match:
        return [f'{skill}: missing YAML frontmatter']
    fields = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if ':' not in line:
            errors.append(f'{skill}: malformed metadata {line!r}')
            continue
        key, value = line.split(':', 1)
        fields[key.strip()] = value.strip()
    name = fields.get('name', '')
    description = fields.get('description', '')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name != skill or len(name) > 64:
        errors.append(f'{skill}: invalid name')
    if not 1 <= len(description) <= 1024:
        errors.append(f'{skill}: invalid description length')
    for ref in re.findall(r'\]\((references/[^)]+)\)', source):
        if not (path.parent / ref).is_file():
            errors.append(f'{skill}: missing {ref}')
    return errors


def main() -> int:
    errors = [err for skill in SKILLS for err in validate(skill)]
    for err in errors:
        print('ERROR:', err)
    if errors:
        return 1
    print(f'PASS: validated {len(SKILLS)} skill frontmatters and local references')
    print('NOTE: Structural validation only; agent behavior not evaluated')
    return 0


if __name__ == '__main__':
    sys.exit(main())
