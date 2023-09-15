class User:
    """
    Ranking system of codewars.com
    """

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, prob_rank):
        if prob_rank > 8 or prob_rank < -8 or prob_rank == 0:
            raise print('error')
        self.progress += User.difference(self.rank, prob_rank)
        while self.progress > 99 and self.rank < 8:
            if self.rank == -1:
                self.rank += 1
            self.rank += 1
            self.progress -= 100
        if self.rank == 8:
            self.progress = 0

    @staticmethod
    def difference(rank, prob_rank):
        if rank == prob_rank:
            return 3
        if rank > 0:
            if prob_rank > 0:
                if prob_rank > rank:
                    return 10 * (prob_rank - rank) ** 2
                else:
                    return 1 if rank - prob_rank == 1 else 0
            else:
                return 1 if rank == 1 and prob_rank == -1 else 0
        else:
            if prob_rank > 0:
                return 10 * (prob_rank + abs(rank) - 1) ** 2
            else:
                if abs(rank) > abs(prob_rank):
                    return 10 * (prob_rank - rank) ** 2
                else:
                    return 1 if abs(prob_rank) - abs(rank) == 1 else 0


if __name__ == '__main__':
    user = User()
    user.inc_progress(1)
    print(user.progress)
    print(user.rank)
