import os
import json

def test_RightKeyNames():
    files = os.listdir("Outputs")
    assert len(files) != 0
    rightKeys = ["id", "timestamp", "direction", "content", "contact"]

    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        for key in jsonFile:
            assert key  in rightKeys

