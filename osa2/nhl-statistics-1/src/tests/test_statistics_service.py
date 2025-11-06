#HUOM!! tehty copilotilla


import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),     # 16
            Player("Lemieux", "PIT", 45, 54),    # 99
            Player("Kurri",   "EDM", 37, 53),    # 90
            Player("Yzerman", "DET", 42, 56),    # 98
            Player("Gretzky", "EDM", 35, 89)     # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.points, 124)

    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Noname")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(all(p.team == "EDM" for p in edm_players))

    def test_team_returns_empty_list_for_unknown_team(self):
        xyz_players = self.stats.team("XYZ")
        self.assertEqual(xyz_players, [])

    def test_top_returns_correct_number_of_players(self):
        top_3 = self.stats.top(3)
        self.assertEqual(len(top_3), 3)
        self.assertEqual(top_3[0].name, "Gretzky")
        self.assertEqual(top_3[1].name, "Lemieux")
        self.assertEqual(top_3[2].name, "Yzerman")

    def test_top_returns_all_players_if_requested_more_than_available(self):
        top_10 = self.stats.top(10)
        self.assertEqual(len(top_10), 5)

if __name__ == "__main__":
    unittest.main()
