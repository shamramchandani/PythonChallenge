import pytest
from greatpersontruth import GreatPersonTruth

@pytest.fixture
def get_truth_obj():
    return GreatPersonTruth()

def test_is_person_great(get_truth_obj):
    p = 'mike'
    assert get_truth_obj.is_person_great(p) == "great"
