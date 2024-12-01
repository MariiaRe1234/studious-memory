import os
import pytest
import json

from solutions.task_08_cars_json import load_from_csv, save_to_json, main


TEST_DATA = """Make,Model,Year
Toyota,Corolla,2005
Ford,F150,2010
Honda,Civic,2015
"""


@pytest.fixture
def setup_csv_file(tmpdir):
    f = tmpdir.join("test.csv")
    f.write(TEST_DATA)
    return f


@pytest.fixture
def setup_json_file(tmpdir):
    return tmpdir.join("test.json")


def test_load_from_csv_returns_correct_data_with_valid_csv(setup_csv_file):
    expected = [
        {'Make': 'Toyota', 'Model': 'Corolla', 'Year': '2005'},
        {'Make': 'Ford', 'Model': 'F150', 'Year': '2010'},
        {'Make': 'Honda', 'Model': 'Civic', 'Year': '2015'}
    ]
    result = load_from_csv(str(setup_csv_file))
    assert result == expected


def test_load_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_from_csv("nonexistent.csv")


@pytest.mark.parametrize("input_data, expected_data", [
    (
        [{'Make': 'Ford', 'Model': 'Focus', 'Year': '2012'}],
        [{"Make": "Ford", "Model": "Focus", "Year": "2012"}]
    ),
    ([], []),
])
def test_save_to_json_saves_correct_data(input_data, expected_data, setup_json_file):
    save_to_json(str(setup_json_file), input_data)
    with open(setup_json_file, 'r') as jf:
        data = json.load(jf)
        assert data == expected_data


def test_save_to_json_file_creation(setup_json_file):
    save_to_json(str(setup_json_file), {"Make": "Ford", "Model": "Focus", "Year": "2012"})
    assert os.path.exists(setup_json_file)


if __name__ == '__main__':
    pytest.main([__file__])
