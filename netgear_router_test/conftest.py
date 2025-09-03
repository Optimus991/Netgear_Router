import pytest
import yaml

@pytest.fixture(scope="session")
def config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)["router"]

@pytest.fixture
def router_ip(config):
    return config["ip"]

@pytest.fixture
def credentials(config):
    return config["username"], config["password"]

@pytest.fixture
def api_url(config):
    return config["api_url"]

@pytest.fixture
def snmp_community(config):
    return config["snmp_community"]
