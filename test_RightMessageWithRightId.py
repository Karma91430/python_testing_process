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

        #Get the specific message based on the unique timestamp
        cur = conn.cursor()
        query = "SELECT * FROM messages WHERE timestamp="+str(jsonFile["timestamp"])
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:

            assert len(row) == 5

            #Get header directly from the database
            header = names = list(map(lambda x: x[0], cur.description))
            #convert it to a dict, easier to get the right paramters afterwards
            message = dict(zip(header, row))
            for key in jsonFile:

                #Verify that the contact exist in the DB and that it is the right contatc_id
                if key == "contact":
                    query = "SELECT * FROM contact WHERE id="+str(message["contact_id"])
                    cur.execute(query)
                    contact = cur.fetchall()
                    print(contact)
                    assert jsonFile[key] == contact[0][1]
                else:
                    assert jsonFile[key] == message[key]
