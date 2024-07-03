import pytest
from project import verify_date
from project import verify_time
from project import add_item

def test_verify_date():
    assert verify_date("01/01/0000") == True
    assert verify_date("13/32/2024") == False
    assert verify_date("ligma") == False

def test_verify_time():
    assert verify_time("23:00") == True
    assert verify_time("09:00 AM") == True
    assert verify_time("24:00") == False
    assert verify_time("13:00 PM") == False

def test_add_item(monkeypatch):
    inputs = ["Walk the dog", "07/04/2024", "23:00"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    add_item()
    with open("tasks.csv") as tasks:
        lines = tasks.readlines()
    assert lines[-1].strip() == "Walk the dog|07/04/2024|23:00"


