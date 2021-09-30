class ChristmasCrackerHappiness:
    def solve(self, N, winner, loser):
        M = len(winner)
        wins = {x: 0 for x in range(N)}
        count = 0
        for i in range(M):
            if wins[winner[i]] == 0:
                count += 1
            wins[winner[i]] += 1
        if N == count:
            return 0
        return N - count - 1

    N_inp0 = 2
    winner_inp0 = []
    loser_inp0 = []
    N_inp1 = 5
    winner_inp1 = [0, 1, 0, 3, 2, 0, 4, 0]
    loser_inp1 = [3, 3, 4, 1, 0, 2, 1, 3]
    N_inp2 = 12
    winner_inp2 = [3, 1, 4, 1, 5, 9, 2, 6]
    loser_inp2 = [5, 3, 5, 8, 9, 7, 9, 3]
    print(solve(solve, N_inp0, winner_inp0, loser_inp0))
    print(solve(solve, N_inp1, winner_inp1, loser_inp1))
    print(solve(solve, N_inp2, winner_inp2, loser_inp2))