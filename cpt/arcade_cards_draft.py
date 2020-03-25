import arcade

WIDTH = 800
HEIGHT = 600

# A class for creating and organizing playing cards
class PlayingCard:
    full_deck = []
    hearts = {}
    diamonds = {}
    spades = {}
    clubs = {}

    def __init__(self, card_value: int, suite: str):
        self.card_value = card_value
        self.suite = suite
        PlayingCard.full_deck.append(self)

    def __str__(self) -> str:
        return f"{self.card_value}, {self.suite}"
    
    @staticmethod
    def make_cards():
        names = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

        i = 0

        while i < 13:
            PlayingCard.hearts[names[i]] = PlayingCard(i+1, 'hearts')
            
            i += 1

        j = 0

        while j < 13:
            PlayingCard.diamonds[names[j]] = PlayingCard(j+1, 'diamonds')
            
            j += 1

        k = 0

        while k < 13:
            PlayingCard.spades[names[k]] = PlayingCard(k+1, 'spades')
            
            k += 1

        l = 0

        while l < 13:
            PlayingCard.clubs[names[l]] = PlayingCard(l+1, 'clubs')
            
            l += 1

PlayingCard.make_cards()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        for card in PlayingCard.hearts.values():
            arcade.draw_xywh_rectangle_filled(card.card_value * 50, 500, 25, 50, arcade.color.RED)

        for card in PlayingCard.diamonds.values():
            arcade.draw_xywh_rectangle_filled(card.card_value * 50, 425, 25, 50, arcade.color.RED)

        for card in PlayingCard.spades.values():
            arcade.draw_xywh_rectangle_filled(card.card_value * 50, 350, 25, 50, arcade.color.BLACK)

        for card in PlayingCard.clubs.values():
            arcade.draw_xywh_rectangle_filled(card.card_value * 50, 275, 25, 50, arcade.color.BLACK)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
