import unittest

from .. simple_game import Game


class TestPygame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_move(self):
        self.game.draw()
        surface = self.game.screen
        surf_w, surf_h = surface.get_size()
        color = surface.get_at((15, 15))
        self.color_cmp(color, 255, 0, 0)

        color = surface.get_at((50, 50))
        self.color_cmp(color, 0, 0, 0)

        for i in range(40): self.game.move_ball()
        self.game.draw()

        color = surface.get_at((15, 15))
        self.color_cmp(color, 0, 0, 0)

        color = surface.get_at((50, 50))
        self.color_cmp(color, 255, 0, 0)

    def color_cmp(self, color, r, g, b):
        self.assertEqual(color.r, r, '\nتابع draw را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertEqual(color.g, g, '\nتابع draw را به درستی پیاده‌سازی نکرده‌اید.')
        self.assertEqual(color.b, b, '\nتابع draw را به درستی پیاده‌سازی نکرده‌اید.')
