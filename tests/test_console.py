#!/usr/bin/python3
""" unittest for the console cpmmand intepreter
"""

import ast
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os
import console
import tests


class TestConsole(unittest.TestCase):
    """Unitetest for our  cmd module"""
    @classmethod
    def setUpClass(self):
        """setup test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """ try removing the file.jason created
            @classmethod means that the method is called on the class
            called after all of the test methods in a class have run
            used to clean up any resources created
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_console(self):
        """pep8 on the console.py"""
        style = pep8.StyleGuide(quite=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(equal, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        """Pep8 on the test_console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_in_test_console(self):
        """Test docstrings  in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Test cmd output: for create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create User")
            self.typing.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]",
                             fake_output.getvalue()[:7])

    def test_all(self):
        """Test cmd output on 'all'"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all Place")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_destroy(self):
        """Test cmd output on 'destroy'"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy")  # what happens if we type 'destroy'
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        """Test cmd output on 'update'"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_class_cmd(self):
        """Test cmd output: <class>.<cmd>"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(ast.literal_eval(ast.parse
                             (fake_output.getvalue(), mode='eval'))))


if __name__ == "__main__":
    unittest.main()
