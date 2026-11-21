from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            need = count[card]  # this many groups must start at `card`
            if need > 0:
                for nxt in range(card, card + groupSize):
                    if count[nxt] < need:
                        return False  # not enough consecutive cards
                    count[nxt] -= need
        return True