from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Priest", 1, 100, 100)
        self.enemy = Hero("Skeleton", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Priest", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_hero_can_not_fight_with_himself(self):
        self.enemy = self.hero

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_is_zero(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as va:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(va.exception))

    def test_enemy_health_is_zero(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as va:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Skeleton. He needs to rest", str(va.exception))

    def test_players_for_draw_battle(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_hero_wins_the_battle_and_stats_increase(self):
        expected_level = self.hero.level + 1
        expected_damage = self.hero.damage + 5
        expected_health = self.hero.health - self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_enemy_wins_the_battle_and_stats_increase(self):
        self.hero, self.enemy = self.enemy, self.hero

        expected_level = self.enemy.level + 1
        expected_damage = self.enemy.damage + 5
        expected_health = self.enemy.health - self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_str_method(self):
        self.assertEqual(f"Hero Priest: 1 lvl\n"
                         f"Health: 100\n"
                         f"Damage: 100\n", self.hero.__str__())


if __name__ == "__main__":
    main()
