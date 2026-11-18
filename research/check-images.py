"""Check that research and model pages only show committed, credited WebP images.

Usage: python research/check-images.py   (exit 1 on any problem)

For every Markdown page directly in research/<topic>/ or models/<name>/:
- each image must be a relative path to a committed .webp file under the topic's img/
- no remote image URLs, and nothing under .cache/
- each file under img/third-party/ must be named in img/third-party/CREDITS.md
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ('research', 'models')
IMG = re.compile(r'!\[[^\]]*\]\(([^)\s]+)[^)]*\)|<img[^>]+src="([^"]+)"', re.I)

tracked = set(subprocess.run(['git', 'ls-files', '-co', '--exclude-standard'], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.splitlines())
problems = []

for page in sorted(p for sec in SECTIONS for p in (ROOT / sec).glob('*/*.md')):
    topic = page.parent
    for m in IMG.finditer(page.read_text(encoding='utf-8')):
        ref = m.group(1) or m.group(2)
        where = f'{page.relative_to(ROOT)}: {ref}'
        if re.match(r'[a-z]+://', ref, re.I):
            problems.append(f'{where} -> remote image; commit a local .webp copy')
            continue
        path = (topic / ref).resolve()
        rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else None
        if '.cache' in pathlib.Path(ref).parts:
            problems.append(f'{where} -> points into gitignored .cache/')
        elif path.suffix.lower() != '.webp':
            problems.append(f'{where} -> not .webp')
        elif not path.is_file():
            problems.append(f'{where} -> file missing')
        elif rel not in tracked:
            problems.append(f'{where} -> not committed (or gitignored)')

for topic in sorted(p for sec in SECTIONS if (ROOT / sec).is_dir() for p in (ROOT / sec).iterdir() if p.is_dir()):
    third = topic / 'img' / 'third-party'
    if third.is_dir():
        credits = third / 'CREDITS.md'
        text = credits.read_text(encoding='utf-8') if credits.is_file() else ''
        if not text:
            problems.append(f'{third.relative_to(ROOT)}: missing CREDITS.md')
        for f in sorted(third.rglob('*')):
            if f.is_file() and f.name != 'CREDITS.md' and f.name not in text:
                problems.append(f'{f.relative_to(ROOT)} -> not listed in CREDITS.md')

print('\n'.join(problems) or 'research images OK')
sys.exit(1 if problems else 0)
