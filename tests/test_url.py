from conftest import run


def test_url_full():
    r = run('url', 'https://user:pass@example.com:8080/path?foo=1&bar=2#frag')
    assert r.returncode == 0
    assert 'protocol: https' in r.stdout
    assert 'username: user' in r.stdout
    assert 'password: pass' in r.stdout
    assert 'hostname: example.com' in r.stdout
    assert 'port: 8080' in r.stdout
    assert 'path: /path' in r.stdout
    assert 'query: foo=1&bar=2' in r.stdout
    assert 'hash: frag' in r.stdout


def test_url_simple():
    r = run('url', 'https://example.com/')
    assert r.returncode == 0
    assert 'protocol: https' in r.stdout
    assert 'hostname: example.com' in r.stdout
    assert 'username' not in r.stdout
    assert 'port' not in r.stdout


def test_url_query_params_listed():
    r = run('url', 'https://example.com/?a=1&b=2')
    assert r.returncode == 0
    assert '- a 1' in r.stdout
    assert '- b 2' in r.stdout


def test_url_no_args():
    r = run('url')
    assert r.returncode != 0
