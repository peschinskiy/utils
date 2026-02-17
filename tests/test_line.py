from conftest import run


def test_line_first():
    r = run('line', '1', input='foo\nbar\nbaz\n')
    assert r.returncode == 0
    assert r.stdout == 'foo\n'


def test_line_middle():
    r = run('line', '2', input='foo\nbar\nbaz\n')
    assert r.returncode == 0
    assert r.stdout == 'bar\n'


def test_line_last():
    r = run('line', '3', input='foo\nbar\nbaz\n')
    assert r.returncode == 0
    assert r.stdout == 'baz\n'


def test_line_out_of_range():
    r = run('line', '99', input='foo\n')
    assert r.returncode == 0
    assert r.stdout == ''


def test_line_no_args():
    r = run('line')
    assert r.returncode != 0
