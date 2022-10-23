# 9/28/22

from KnowledgeManager.Utils.common_functions import print_banner_line
from common_test_functions import capture_output
from test_base import TestBase

class TestCommonFunctions(TestBase):

    def test_print_header_line_returns_string_of_correct_length(self):

        output = capture_output(print_banner_line, "", 51)
        self.assertEqual(len(output), 52)

        output = capture_output(print_banner_line, "", 50)
        self.assertEqual(len(output), 51)

        output = capture_output(print_banner_line, "12345", 51)
        self.assertEqual(len(output), 52)

        output = capture_output(print_banner_line, "12345", 50)
        self.assertEqual(len(output), 51)

        output = capture_output(print_banner_line, "12345678", 51)
        self.assertEqual(len(output), 52)

        output = capture_output(print_banner_line, "12345678", 50)
        self.assertEqual(len(output), 51)

        output = capture_output(print_banner_line, "", 10)
        self.assertEqual(output, "----------\n")

        output = capture_output(print_banner_line, "", 11)
        self.assertEqual(output, "-----------\n")

        output = capture_output(print_banner_line, "12345", 10)
        self.assertEqual(output, "--12345---\n")

        output = capture_output(print_banner_line, "12345", 11)
        self.assertEqual(output, "---12345---\n")

        output = capture_output(print_banner_line, "12345678", 10)
        self.assertEqual(output, "-12345678-\n")

        output = capture_output(print_banner_line, "12345678", 11)
        self.assertEqual(output, "-12345678--\n")

        output = capture_output(print_banner_line, "123456789", 5)
        self.assertEqual(output, "123456789\n")

        output = capture_output(print_banner_line, "123456789", 9)
        self.assertEqual(output, "123456789\n")

        output = capture_output(print_banner_line, "123456789", 10)
        self.assertEqual(output, "123456789-\n")


