import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'INTERNAL') == 1171

    with pytest.raises(AttributeError):
        count_ocurrences('data/jobs.csv', -1)

    with pytest.raises(AttributeError):
        count_ocurrences('data/jobs.csv', None)

    with pytest.raises(AttributeError):
        count_ocurrences('data/jobs.csv', [])

    with pytest.raises(AttributeError):
        count_ocurrences('data/jobs.csv', {})
