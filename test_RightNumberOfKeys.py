import os
import json

def test_RightNumberOfKeys():
    files = os.listdir("Outputs")
    assert len(files) != 0
    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        assert len(jsonFile) == 5



