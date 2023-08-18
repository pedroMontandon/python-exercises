import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('Chapolin', 'colorado')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 4)
    assert encrypt_message('Chapolin', 56) == ''
