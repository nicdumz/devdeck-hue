import json
import os
import phue
import pytest


@pytest.fixture
def bridge_ip():
    return '192.168.1.241'


@pytest.fixture
def mock_env_user_home(monkeypatch, tmpdir):
    monkeypatch.setenv(phue.USER_HOME, tmpdir)


@pytest.fixture
def setup_hue(mock_env_user_home, bridge_ip):
    path = os.path.join(os.getenv(phue.USER_HOME), '.python_hue')
    data = {}
    data[bridge_ip] = dict(username='fake_test_username')
    json.dump(data, open(path, 'w'))