
import os
import json

def test_noFileGenerated():
    files = os.listdir("Outputs")
    assert len(files) != 0
