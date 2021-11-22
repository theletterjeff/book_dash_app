from contextlib import contextmanager
import os
import sqlite3 as sql

@contextmanager
def connect(path: os.PathLike):
    con = sql.connect(path)
    yield con
    con.commit()
    con.close()