#!/usr/bin/python3


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.temp_stdout = StringIO()

    def tearDown(self):
        self.temp_stdout.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        output = f.getvalue().strip()
        self.assertTrue(len(output) == 36)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
        output = f.getvalue().strip()
        self.assertTrue("BaseModel" in output)
        self.assertTrue(obj_id in output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.assertFalse(f.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
        self.assertTrue(f.getvalue().strip() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        self.console.onecmd("count BaseModel")
        self.assertTrue(mock_stdout.getvalue().strip() == "0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} first_name 'John'")
        self.assertIn('** value conversion error **', f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_dict(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} {{'first_name': 'John', 'age': 89}}")
        self.assertIn('** value conversion error **', f.getvalue())


if __name__ == "__main__":
    unittest.main()
