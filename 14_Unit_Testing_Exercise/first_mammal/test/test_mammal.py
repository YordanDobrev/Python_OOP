from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Cow", "land_animal", "Moo")

    def test_correct_init(self):
        self.assertEqual("Cow", self.mammal.name)
        self.assertEqual("land_animal", self.mammal.type)
        self.assertEqual("Moo", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_correct_sound_from_the_animal(self):
        self.assertEqual(f"Cow makes Moo", self.mammal.make_sound())

    def test_correct_kingdom_is_returned(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_correct_animal_information_is_returned(self):
        self.assertEqual(f"Cow is of type land_animal", self.mammal.info())


if __name__ == "__main_":
    main()
