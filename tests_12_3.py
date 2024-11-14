from tests_12_1 import Runner
import unittest
from tests_12_2 import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self,):
        r1 = Runner('Jerry')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self,):
        r1 = Runner('Jerry')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Jerry')
        r2 = Runner('Tom')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_variants = []

    def setUp(self):
        self.runner_1 = Runner('Ben', 10)
        self.runner_2 = Runner('Tom', 9)
        self.runner_3 = Runner('Niki', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_variants):
            print(f'{i + 1}. {elem}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Niki')
        self.all_results['Тест первого раунда'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Niki')
        self.all_results['Тест второго раунда'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Niki')
        self.all_results['Тест третьего раунда'] = result


if __name__ == '__main__':
    unittest.main()