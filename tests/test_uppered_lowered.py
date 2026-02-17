from conftest import run


def test_uppered_basic():
    r = run('uppered', input='hello world\n')
    assert r.returncode == 0
    assert r.stdout == 'HELLO WORLD\n'


def test_uppered_already_upper():
    r = run('uppered', input='HELLO\n')
    assert r.returncode == 0
    assert r.stdout == 'HELLO\n'


def test_uppered_mixed():
    r = run('uppered', input='Hello World\n')
    assert r.returncode == 0
    assert r.stdout == 'HELLO WORLD\n'


def test_lowered_basic():
    r = run('lowered', input='HELLO WORLD\n')
    assert r.returncode == 0
    assert r.stdout == 'hello world\n'


def test_lowered_already_lower():
    r = run('lowered', input='hello\n')
    assert r.returncode == 0
    assert r.stdout == 'hello\n'


def test_lowered_mixed():
    r = run('lowered', input='Hello World\n')
    assert r.returncode == 0
    assert r.stdout == 'hello world\n'
