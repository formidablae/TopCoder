class DivideLoot:
    def verify(  # self,
            N,
            loot):
        if N > len(loot) or len(loot) > 2 * N:
            return "impossible"
        elif len(loot) == N:
            if loot.count(loot[0]) == N:
                return "possible"
            else:
                return "impossible"
        else:
            loot_list = list(loot)
            loot_list.sort(reverse=True)
            # print(loot_list)
            assigned = [0] * N
            i = 0
            goingdown = True
            while len(loot_list) > 0:
                assigned[i] = assigned[i] + loot_list.pop(0)
                if i < N - 1 and goingdown:
                    i += 1
                elif i < N and not goingdown:
                    i -= 1
                else:
                    goingdown = False
            for j in range(1, N):
                if assigned[i - 1] != assigned[i]:
                    return "impossible"
            return "possible"


    N_inp0 = 1
    loot_0 = [47]
    N_inp1 = 3
    loot_1 = [10, 8, 10, 1, 1]
    N_inp2 = 3
    loot_2 = [3, 9, 10, 7, 1]
    N_inp3 = 6
    loot_3 = [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
    N_inp4 = 2
    loot_4 = [40, 1, 42]
    print(verify(N_inp0, loot_0))
    print(verify(N_inp1, loot_1))
    print(verify(N_inp2, loot_2))
    print(verify(N_inp3, loot_3))
    print(verify(N_inp4, loot_4))
