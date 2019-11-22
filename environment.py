import random


class Environment:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self):
        self.sum_player = 0
        self.usable_ace_player = False

        self.dealer_initial_card = 0
        self.sum_dealer = 0
        self.usable_ace_dealer = False

        self.player_sticked = False

    def get_card(self):
        """
        Returns a random card with value from 1 to 10.
        """
        return random.choice(self.cards)

    def deal_player(self):
        """
        Deals the card until player has sum 12 or greater.
        """
        while self.sum_player < 12:
            self.hit()

    def deal_dealer(self):
        """
        Deals cards to dealer until 17 or greater.
        Remembers first card of the dealer from 2 to 11.
        """
        while self.sum_dealer < 17:
            self.sum_dealer, self.usable_ace_dealer = self.get_next_state(
                self.sum_dealer,
                self.usable_ace_dealer
            )
            if self.dealer_initial_card == 0:
                self.dealer_initial_card = self.sum_dealer

    def is_end(self):
        """
        Checks if it is the end of the game.
        """
        return self.sum_player > 21 or self.player_sticked

    def get_next_state(self, sum_cards, usable_ace):
        """
        Go to the next state with with given sum and usable ace info.
        """
        card = self.get_card()

        if card == 1 and sum_cards + 11 <= 21:
            card = 11
            usable_ace = True

        sum_cards += card

        if sum_cards > 21 and usable_ace:
            sum_cards -= 10
            usable_ace = False
        return sum_cards, usable_ace

    def stick(self):
        """
        Mark that player sticked.
        """
        self.player_sticked = True

    def get_reward(self):
        """
        Return the reward for the game.
        """
        if self.sum_player > 21:
            return -1
        if self.sum_dealer > 21:
            return 1

        if self.sum_player > self.sum_dealer:
            return 1
        elif self.sum_player == self.sum_dealer:
            return 0
        else:
            return -1

    def hit(self):
        """
        Update state of the player.
        """
        self.sum_player, self.usable_ace_player = self.get_next_state(
            self.sum_player,
            self.usable_ace_player
        )

    def get_state(self):
        """
        Get state of the player.
        """
        return self.sum_player, self.usable_ace_player, self.dealer_initial_card