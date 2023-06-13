import os
import json

def test_noFile():
    files = os.listdir("Outputs")
    assert len(files) != 0

def test_NumberOfKeys():
    files = os.listdir("Outputs")
    assert len(files) != 0
    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        assert len(jsonFile) == 5


def test_RightKeys():
    files = os.listdir("Outputs")
    assert len(files) != 0
    rightKeys = ["id", "timestamp", "direction", "content", "contact"]

    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        for key in jsonFile:
            assert key  in rightKeys


def test_RightType():
    rightKeys = {"id":1, "timestamp":1, "direction":"String", "content":"String", "contact":"String"}
    files = os.listdir("Outputs")
    assert len(files) != 0

    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        for key in jsonFile:
            assert type(jsonFile[key]) == type(rightKeys[key])

