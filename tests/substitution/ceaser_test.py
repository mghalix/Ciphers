import sys

sys.path.append("../..")
from substitution import ceaser
import pytest


@pytest.mark.parametrize(
    "plaintext, key, expected_cipher",
    [
        ("abc", 1, "bcd"),
        ("a", 2, "c"),
        ("a", 3, "d"),
        ("z", 1, "a"),
        ("meet me after the ali party", 3, "phhw ph diwhu wkh dol sduwb"),
        ("i love coffee", 7, "p svcl jvmmll"),
    ],
)
def test_encrypt(plaintext, key, expected_cipher):
    assert ceaser.encrypt(plaintext, key) == expected_cipher


@pytest.mark.parametrize(
    "ciphertext, key, expected_plain",
    [
        ("bcd", 1, "abc"),
        ("c", 2, "a"),
        ("d", 3, "a"),
        ("a", 1, "z"),
        ("phhw ph diwhu wkh dol sduwb", 3, "meet me after the ali party"),
        ("p svcl jvmmll", 7, "i love coffee"),
    ],
)
def test_decrypt(ciphertext, key, expected_plain):
    assert ceaser.decrypt(ciphertext, key) == expected_plain
