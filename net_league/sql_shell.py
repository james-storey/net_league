#!/usr/bin/env python
import sqlite3
from tabulate import tabulate

def run():
    con = sqlite3.connect('netrunner.db')
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print("Enter SQL commands to execute on the netrunner league database.")
    print("Enter a blank line to exit")

    while True:
        line = input("> ")
        if line == "":
            break
        buffer += line
        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                cur.execute(buffer)
                if buffer.lstrip().upper().startswith("SELECT"):
                    headers = []
                    rows = cur.fetchall()
                    for title in cur.description:
                        headers.append(title[0])
                    print(tabulate(rows,headers=headers, tablefmt='orgtbl'))
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
            buffer = ""

    con.close()

if __name__ == "__main__":
    run()
