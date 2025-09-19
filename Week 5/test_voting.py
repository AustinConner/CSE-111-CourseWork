import pytest
from voting import can_vote

def test_can_vote_younger():
    assert can_vote(7) == False

def test_can_vote_older():
    assert can_vote(26) == True

def test_can_vote_equal():
    assert can_vote(18) == True

def test_can_vote_canada_1970():
    assert can_vote(21, 21)
    assert not can_vote(19, 21) 
    assert can_vote(30, 21) 
    assert can_vote(22, 21)

    # Verify US standard parm is not getting set.
    assert not can_vote(17, 21)
    assert not can_vote(18, 21)


pytest.main(["-v", "--tb=line", "-rN", __file__])