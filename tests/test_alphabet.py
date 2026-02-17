from conftest import run


def test_alphabet_output():
    r = run('alphabet')
    assert r.returncode == 0
    lines = r.stdout.splitlines()
    assert lines[0] == 'abcdefghijklmnopqrstuvwxyz'
    assert lines[1] == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_alphabet_completeness():
    r = run('alphabet')
    lower = r.stdout.splitlines()[0]
    upper = r.stdout.splitlines()[1]
    assert len(lower) == 26
    assert len(upper) == 26
