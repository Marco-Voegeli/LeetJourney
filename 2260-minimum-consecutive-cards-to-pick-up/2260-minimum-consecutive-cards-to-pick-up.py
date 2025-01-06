class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        max_val = 10**6 + 1
        score = max_val
        viewed_cards = {}
        for i in range(len(cards)):
            card = cards[i]
            if card in viewed_cards:
                new_score =(i + 1 - viewed_cards[card])
                score = min(score, new_score)
            viewed_cards[card] = i
        if score == max_val:
            return -1
        return score