import re
from conftest import run


def test_ymd_format():
    r = run('ymd')
    assert r.returncode == 0
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.stdout), f'unexpected output: {r.stdout!r}'


def test_ymd_no_trailing_newline():
    r = run('ymd')
    assert not r.stdout.endswith('\n')
