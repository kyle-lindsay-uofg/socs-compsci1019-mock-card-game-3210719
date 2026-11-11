import unittest
from unittest.mock import mock_open, patch
from card_game import Game
from card_game import LoadCSV
from card_game.communication import ConsoleInOut
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.Deck import *
from card_game.Game import *
from card_game.LoadCSV import *

class test_task(unittest.TestCase):

    @patch('builtins.input', return_value='18')
    def test_get_input_integer(self, mock_input):
        self.assertEqual(ConsoleInOut.get_input_integer('message'), 18)

    @patch('builtins.input', side_effect=['Derek', '3'])
    def test_get_game_info(self, mock_input):
        self.assertEqual(Game.get_game_info(), ('Derek', 3)) # returns name and number of players, so 'Derek' and 3, not just 3

    @patch('builtins.input', return_value='abc')
    def test_get_integer_max_attempts(self, mock_get_string):
        self.assertEqual(ConsoleInOut.get_integer(), -1)
        mock_get_string.assert_called()
        self.assertEqual(mock_get_string.call_count, 5)

    @patch("builtins.open", new_callable=mock_open, read_data='Derek\nXi')
    def test_get_csv_rows(self, mock_open):
        self.assertEqual(LoadCSV.get_csv_rows('file.txt')[1][0], 'Xi')

    @patch('card_game.card.entity.Deck.random.randint', return_value=0)
    def test_play_a_card_from_deck_random(self, mock_random):
        deck = create_deck()
        first_card = deck[0]
        self.assertEqual(play_a_card_from_deck(deck), first_card)