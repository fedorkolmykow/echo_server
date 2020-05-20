import pytest
import server
from freezegun import freeze_time


@pytest.mark.parametrize('mes,exp', [
    ('echo message', 'message'),
    ('stop', 'Server stopped'),
    ('something random', f'Доступны следующие команды: {",".join(server.COMMANDS)}'),
])
def test_process_message(mes, exp):
    out = server.process_message(mes)
    assert out == exp


def test_process_message_calendar():
    with freeze_time("1997.01.03 12:12"):
        out = server.process_message('calendar')
    assert out == '1997.01.03 12:12'


