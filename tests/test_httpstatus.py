from conftest import run


def test_list_all():
    r = run('httpstatus')
    assert r.returncode == 0
    assert '200 OK' in r.stdout
    assert '404 Not Found' in r.stdout
    assert '500 Internal Server Error' in r.stdout


def test_lookup_exact():
    r = run('httpstatus', '404')
    assert r.returncode == 0
    assert '404 Not Found' in r.stdout


def test_lookup_case_insensitive():
    r = run('httpstatus', 'not found')
    assert r.returncode == 0
    assert '404 Not Found' in r.stdout


def test_lookup_no_match():
    r = run('httpstatus', 'zzznomatch')
    # grep exits 1 when no lines match
    assert r.returncode != 0
    assert r.stdout == ''


def test_lookup_teapot():
    r = run('httpstatus', '418')
    assert r.returncode == 0
    assert "418 I'm a teapot" in r.stdout
