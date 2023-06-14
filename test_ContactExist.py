import os
import json
import sqlite3

def test_contactExist():
    conn = None
    try:
        conn = sqlite3.connect("messaging.db")
    except Exception as e:
        print(e)

    files = os.listdir("Outputs")
    assert len(files) != 0

    for file in files:
        f = open("Outputs/"+file)
        jsonFile = json.load(f)

        #Get all the contacts in the database
        cur = conn.cursor()
        query = "SELECT * FROM contact WHERE name='"+str(jsonFile["contact"])+"'"
        cur.execute(query)

        rows = cur.fetchall()
        #Verify that the DB return at list one contact
        assert len(rows) != None

test_contactExist()        