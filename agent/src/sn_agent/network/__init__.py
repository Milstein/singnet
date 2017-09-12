from jinja2.utils import import_string

from sn_agent.network.settings import NetworkSettings
from sn_agent.agent.test import TestAgent


def setup_network(app):
    settings = NetworkSettings()
    agent = TestAgent(app, '613cfd03-14a2-45dd-a94c-3c7798aca958')
    network_klass = import_string(settings.NETWORK_CLASS)
    app['network'] = network_klass(app, agent)
