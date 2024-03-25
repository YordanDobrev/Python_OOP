from unittest import TestCase, main

#from first_test_worker.worker import Worker


class TestWorker(TestCase):
    pass

    def setUp(self):
        self.worker = Worker("Tom", 5000, 100)

    def test_correct_init(self):
        self.assertEqual("Tom", self.worker.name)
        self.assertEqual(5000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_is_enough(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_worker_when_energy_is_not_enough(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_if_rest_is_complete(self):
        exp_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(exp_energy, self.worker.energy)

    def test_get_info_for_the_worker(self):
        self.assertEqual(f'Tom has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
