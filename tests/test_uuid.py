import re
from conftest import run

UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
)


def test_uuid_format():
    r = run('uuid')
    assert r.returncode == 0
    assert UUID_RE.match(r.stdout), f'unexpected output: {r.stdout!r}'


def test_uuid_no_trailing_newline():
    r = run('uuid')
    assert not r.stdout.endswith('\n')


def test_uuid_unique():
    results = {run('uuid').stdout for _ in range(5)}
    assert len(results) == 5, 'UUIDs should be unique'
