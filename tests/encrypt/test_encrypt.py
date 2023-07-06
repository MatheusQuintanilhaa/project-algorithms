import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    pass

# Teste para chave ímpar
assert encrypt_message("message", 3) == "sem_egas"
# assert encrypt_message("trybe", 5) == "ebyrt"


# Teste para chave par
assert encrypt_message("message", 4) == "ega_ssem"
# assert encrypt_message("trybe", 2) == "eybtr"

# Teste para chave inválido
assert encrypt_message("message", -2) == "egassem"
# assert encrypt_message("trybe", 8) == "ebyrt"

# Teste para tipos incorretos de entrada
with pytest.raises(TypeError, match="tipo inválido para message"):
    encrypt_message(5, 3)

with pytest.raises(TypeError, match="tipo inválido para key"):
    encrypt_message("trybe", 3.9)
