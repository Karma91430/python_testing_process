import os
import json
import sqlite3

def test_RightMessageWithRightId():
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

        cur = conn.cursor()
        query = "SELECT * FROM messages WHERE timestamp="+str(jsonFile["timestamp"])
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:

            assert len(row) == 5
            
            inputTuple = (("id", row[0]), ("timestamp", row[1]), ("direction", row[2]), ("content", row[3]), ("contact", row[4]))
            message = dict((x, y) for x, y in inputTuple)
            for key in jsonFile:

                if key == "contact":
                    query = "SELECT * FROM contact WHERE id="+str(message["contact"])
                    cur.execute(query)
                    contact = cur.fetchall()
                    print(contact)
                    assert jsonFile[key] == contact[0][1]
                else:
                    assert jsonFile[key] == message[key]
