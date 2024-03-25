from unittest import TestCase, main

from third_list.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "Hello")

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_if_added_element_is_integer(self):
        with self.assertRaises(ValueError) as va:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(va.exception))

    def test_if_the_element_is_added_correctly(self):
        exp = self.i_list.add(5)

        self.i_list.add(5)

        self.assertEqual(exp, self.i_list.get_data())

    def test_if_element_is_not_out_of_range_raise_Index_error(self):
        with self.assertRaises(IndexError) as indx:
            self.i_list.remove_index(10000)

        self.assertEqual("Index is out of range", str(indx.exception))

    def test_if_element_is_removed_from_the_list(self):
        self.i_list.remove_index(1)

        self.assertEqual([1, 3], self.i_list.get_data())

    def test_if_element_is_out_of_range_raise_Index_error(self):
        with self.assertRaises(IndexError) as indx:
            self.i_list.get(10000)

        self.assertEqual("Index is out of range", str(indx.exception))

    def test_if_index_is_in_the_correct_range(self):
        exp_result = self.i_list.get(1)

        self.assertEqual(2, exp_result)

    def test_correct_index_when_element_is_insert(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(10000, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correct_type_is_inserted(self):
        with self.assertRaises(ValueError) as va:
            self.i_list.insert(1, 10.40)

        self.assertEqual("Element is not Integer", str(va.exception))

    def test_correct_data_is_being_added(self):
        expected_result = self.i_list.get_data().copy()

        expected_result.insert(1, 5)
        self.i_list.insert(1, 5)

        self.assertEqual(expected_result, self.i_list.get_data())

    def test_biggest_element_in_the_collection(self):
        expec_result = self.i_list.get_biggest()

        self.assertEqual(3, expec_result)

    def test_correct_index_is_being_returned(self):
        result = self.i_list.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
