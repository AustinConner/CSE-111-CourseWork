from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"

def test_extract_family_name():
        """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's family name
    """
        assert extract_family_name("Brown; Sally") == "Brown"

def test_extract_given_name():
      assert extract_given_name("Brown; Sally") == "Sally"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
