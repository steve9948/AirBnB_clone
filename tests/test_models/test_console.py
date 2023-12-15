import unittest
from unittest.mock import patch, Mock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_cmd.onecmd('quit'))
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_EOF_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_cmd.onecmd('EOF'))
            self.assertEqual(mock_stdout.getvalue(), "\n")

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.emptyline()
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_help_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd('help')
            self.assertIn("List available commands", mock_stdout.getvalue())

    def test_unknown_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd('unknown_cmd')
            self.assertIn("** Unknown command:", mock_stdout.getvalue())

    def test_custom_prompt(self):
        self.assertEqual(self.hbnb_cmd.prompt, "(hbnb) ")

    def test_cmdloop_exit(self):
        def test_cmdloop_exit(self):
            with patch('builtins.input', side_effect=['quit']):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    HBNBCommand().cmdloop()
                    self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=Mock)
    def test_create_success(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.new') as mock_new, \
                patch('models.engine.file_storage.storage.save') as mock_save:
            console.do_create("BaseModel")
            mock_new.assert_called()
            mock_save.assert_called_once()
            created_id = mock_stdout.getvalue().strip()
            self.assertTrue(created_id)

    @patch('sys.stdout', new_callable=Mock)
    def test_create_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.new') as mock_new, \
                patch('models.engine.file_storage.storage.save') as mock_save:
            console.do_create("NonExistentClass")
            mock_new.assert_not_called()
            mock_save.assert_not_called()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_show_success(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.123': 'test_instance'}
            console.do_show("BaseModel 123")
            self.assertIn(
                "['BaseModel', '123', 'BaseModel.123', {'BaseModel.123': 'test_instance'}]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_show_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_show("NonExistentClass 123")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_show_instance_id_missing(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_show("BaseModel")
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_destroy_success(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all, \
                patch('models.engine.file_storage.storage.save') as mock_save:
            mock_all.return_value = {'BaseModel.123': 'test_instance'}
            console.do_destroy("BaseModel 123")
            mock_save.assert_called_once()
            self.assertIn("Instance deleted successfully",
                          mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_destroy_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_destroy("NonExistentClass 123")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_destroy_instance_id_missing(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_destroy("BaseModel")
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_destroy_no_instance_found(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_destroy("BaseModel 123")
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_all_success(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.123': 'test_instance'}
            console.do_all("BaseModel")
            self.assertIn(
                "['BaseModel', '123', 'BaseModel.123', {'BaseModel.123': 'test_instance'}]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_all_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        console.do_all("NonExistentClass")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_success(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all, \
                patch('models.engine.file_storage.storage.save') as mock_save:
            mock_all.return_value = {'BaseModel.123': 'test_instance'}
            console.do_update("BaseModel 123 email 'new_email'")
            mock_save.assert_called_once()
            self.assertIn(
                "{'BaseModel', '123', 'email', 'new_email'}", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        console.do_update("NonExistentClass 123 email 'new_email'")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_instance_id_missing(self, mock_stdout):
        console = HBNBCommand()
        console.do_update("BaseModel email 'new_email'")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_no_instance_found(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_update("BaseModel 123 email 'new_email'")
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_attribute_name_missing(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_update("BaseModel")
            self.assertIn("** attribute name missing **",
                          mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=Mock)
    def test_update_value_missing(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.engine.file_storage.storage.all') as mock_all:
            console.do_update("BaseModel 123 email")
            self.assertIn("** value missing **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
