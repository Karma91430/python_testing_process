import os
import json

def test_RightKeyTypes():
    rightKeys = {"id":1, "timestamp":1, "direction":"String", "content":"String", "contact":"String"}
    files = os.listdir("Outputs")
    assert len(files) != 0

    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        for key in jsonFile:
            assert type(jsonFile[key]) == type(rightKeys[key])
