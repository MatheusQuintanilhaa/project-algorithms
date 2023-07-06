import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 4) == "ega_ssem"
    assert encrypt_message("message", -2) == "egassem"

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 3)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", 3.9)
