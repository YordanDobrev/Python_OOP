from unittest import TestCase, main
from second_cat.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Frank")

    def test_correct_init(self):
        self.assertEqual("Frank", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_is_well_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_is_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_cat_size_is_getting_bigger(self):
        expect = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expect, self.cat.size)

    def test_cat_cannot_fall_asleep_if_not_fed_raises_an_error(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
