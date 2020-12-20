from . import HungarianCard, Rank


def next_card(card: HungarianCard) -> HungarianCard:
    rank = {
        Rank.VII: Rank.VIII,
        Rank.VIII: Rank.IX,
        Rank.IX: Rank.X,
        Rank.X: Rank.UNDER,
        Rank.UNDER: Rank.UPPER,
        Rank.UPPER: Rank.KING,
        Rank.KING: Rank.ACE,
        Rank.ACE: Rank.VII,
    }.get(card.rank, Rank.UNKNOWN_RANK)

    return HungarianCard(rank, card.suit)