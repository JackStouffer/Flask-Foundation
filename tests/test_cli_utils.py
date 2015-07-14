import mock
import unittest

from appname.util import cli


class TestCliUtils(unittest.TestCase):
    def test_yes(self):
        """ Test Yes cases """
        mock_one = mock.MagicMock()

        with mock.patch('appname.util.cli.get_input', mock_one):
            mock_one.return_value = 'y'
            result = cli.yes_no('Test y')
            self.assertIsNotNone(result)
            mock_one.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_one):
            mock_one.return_value = 'yes'
            result = cli.yes_no('Test yes')
            self.assertIsNotNone(result)
            mock_one.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_one):
            mock_one.return_value = 'Y'
            result = cli.yes_no('Test Y')
            self.assertIsNotNone(result)
            mock_one.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_one):
            mock_one.return_value = 'Yes'
            result = cli.yes_no('Test Yes')
            self.assertIsNotNone(result)

    def test_no(self):
        """ Test No cases """
        mock_input = mock.MagicMock()

        with mock.patch('appname.util.cli.get_input', mock_input):
            mock_input.return_value = 'n'
            result = cli.yes_no('Test n')
            self.assertIsNotNone(result)
            mock_input.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_input):
            mock_input.return_value = 'no'
            result = cli.yes_no('Test no')
            self.assertIsNotNone(result)
            mock_input.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_input):
            mock_input.return_value = 'N'
            result = cli.yes_no('Test N')
            self.assertIsNotNone(result)
            mock_input.reset_mock()

        with mock.patch('appname.util.cli.get_input', mock_input):
            mock_input.return_value = 'No'
            result = cli.yes_no('Test No')
            self.assertIsNotNone(result)

    def test_no_bool(self):
        """ Test exception case """
        mock_input = mock.MagicMock()

        with mock.patch('appname.util.cli.get_input', mock_input):
            mock_input.return_value = 'WRONG'
            mock_input.side_effect = ValueError

            with self.assertRaises(ValueError):
                cli.yes_no('Test Wrong')
