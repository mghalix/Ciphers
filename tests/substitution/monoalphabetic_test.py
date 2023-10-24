import sys
import pytest

sys.path.append("../../")
from substitution import monoalphabetic


@pytest.mark.parametrize(
    "plaintext, ckey, expected_cipher",
    [
        (
            "abcdefghijklmnopqrstuvwxyz",
            "dkvqfibjwpescxhtmyauolrgzn",
            "dkvqfibjwpescxhtmyauolrgzn",
        ),
        (
            "if we wish to replace letters",
            "dkvqfibjwpescxhtmyauolrgzn",
            "wi rf rwaj uh yftsdvf sfuufya",
        ),
        (
            "i study computer security",
            "abcdefghijklmnopqrstuvwxyz"[::-1],
            "r hgfwb xlnkfgvi hvxfirgb",
        ),
    ],
)
def test_cipher(plaintext, ckey, expected_cipher):
    assert monoalphabetic.cipher(plaintext, ckey) == expected_cipher


@pytest.mark.parametrize(
    "ciphertext, ckey, expected_plain",
    [
        (
            "dkvqfibjwpescxhtmyauolrgzn",
            "dkvqfibjwpescxhtmyauolrgzn",
            "abcdefghijklmnopqrstuvwxyz",
        ),
        (
            "wi rf rwaj uh yftsdvf sfuufya",
            "dkvqfibjwpescxhtmyauolrgzn",
            "if we wish to replace letters",
        ),
        (
            "r hgfwb xlnkfgvi hvxfirgb",
            "abcdefghijklmnopqrstuvwxyz"[::-1],
            "i study computer security",
        ),
    ],
)
def test_decipher(ciphertext, ckey, expected_plain):
    assert monoalphabetic.decipher(ciphertext, ckey) == expected_plain
