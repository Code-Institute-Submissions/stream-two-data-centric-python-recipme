import os
import pymysql
import recipme
import unittest
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

class TestRecipme(unittest.TestCase):
    def test_read_all_from_one_table(self):
        table = "User"
        query = recipme.read_db(table)
        result = query.read_all_from_one_table()

        self.assertEqual(type(result), list)
