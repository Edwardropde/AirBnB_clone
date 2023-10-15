#!/usr/bin/python3


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.temp_stdout = StringIO()
        self.temp_stderr = StringIO()

    def tearDown(self):
        self.temp_stdout.close()
        self.temp_stderr.close()

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
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("all")
        output = f.getvalue().strip()
        self.assertTrue("BaseModel" in output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        h = "Counts the number of instances of a class."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.stderr', new_callable=StringIO)
    def test_update(self, mock_stdout, mock_stderr):
        self.console.onecmd("create BaseModel")
        obj_id = self.temp_stdout.getvalue().strip()
        self.console.onecmd(f"update BaseModel {obj_id} first_name 'John'")
        output_stdout = mock_stdout.getvalue()
        output_stderr = mock_stderr.getvalue()
        print("Captured stdout:")
        print(output_stdout)
        print("Captured stderr:")
        print(output_stderr)
        self.assertIn('** no instance found **', output_stdout)


if __name__ == "__main__":
    unittest.main()
