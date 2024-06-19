import unittest
from src.full_name_printer import get_formatted_name

class NamesTestCase (unittest.TestCase):

    def test_last_occupation_middle_name (self):

        # Do names like 'N. Nkomo, roboticist' work?
        formatted_name = get_formatted_name ("nkomo", "roboticist", "nigel")
        self.assertEqual (formatted_name, "N. Nkomo, roboticist")

if __name__ == "__main__":
    unittest.main ()