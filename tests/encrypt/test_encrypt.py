from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("ragatanga", "2")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)

    assert encrypt_message("ragatanga", 10) == "agnatagar"

    assert encrypt_message("ragatanga", 3) == "gar_agnata"

    assert encrypt_message("ragatanga", 4) == "agnat_agar"
