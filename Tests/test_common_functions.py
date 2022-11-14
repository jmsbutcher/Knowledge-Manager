# 9/28/22

from KnowledgeManager.Utils.common_functions import print_banner_line, \
    extract_trailing_int, PrefixNotFoundException
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


    def test_extract_int_after_prefix_extracts_correctly(self):

        extracted = extract_trailing_int("New Document1", "New Document")
        self.assertEqual(extracted, 1)

        extracted = extract_trailing_int("New Document34", "New Document")
        self.assertEqual(extracted, 34)

        extracted = extract_trailing_int("New Document 999", "New Document")
        self.assertEqual(extracted, 999)


    def test_extract_int_after_prefix_extracts_correctly_with_gaps(self):

        extracted = extract_trailing_int("New Document1", "New Document")
        self.assertEqual(extracted, 1)

        extracted = extract_trailing_int("New Document34b11", "New Document")
        self.assertEqual(extracted, 11)

        extracted = extract_trailing_int("4New Document 999", "New Document")
        self.assertEqual(extracted, 999)


    def test_extract_int_after_prefix_returns_None_when_last_not_int(self):

        extracted = extract_trailing_int("New Document", "New Document")
        self.assertIsNone(extracted)

        extracted = extract_trailing_int("New Document_abc", "New Document")
        self.assertIsNone(extracted)


    def test_extract_int_after_prefix_exception_when_prefix_not_found(self):

        func = extract_trailing_int
        self.assertRaises(PrefixNotFoundException, func, "", "New Document")
        self.assertRaises(PrefixNotFoundException, func, "NewDocumnt23", "New Document")


