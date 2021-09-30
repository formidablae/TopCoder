# import math
#
# class ChristmasLightsFixing:
#     def fixingTime(self, N, step):
#         print("Bulbs =", list(range(N)))
#         print("Step =", step)
#         r = 1
#         count_tests = {}
#         lex_test = []
#         found = 0
#         indexes = [-1]
#         considering = []
#         while r < 5 and i < 5:
#             print("lex_test =", lex_test)
#             print("count_tests =", count_tests)
#             print("r =", r, "step =", step)
#             print("found =", found, "inner_r =", inner_r)
#             nextround = math.factorial(N) // (math.factorial(max(0, N - r)) * math.factorial(max(0, r)))
#             print("nextround =", nextround)
#             if step < nextround:
#                 while True:
#                     considering = considering + list(range())
#                     indexes[found] += 1
#                     print("enter if step < nextround", step, "<", nextround)
#                     # lex_test.append(r - inner_r - 1)
#                     # found += 1
#                     # i += 1
#             else:
#                 step -= nextround
#                 count_tests[r] = nextround
#                 r += 1
#                 indexes.append(-1)
#         return 0
#
#     N_inp0 = 5
#     step_inp0 = 16
#     N_inp1 = 40
#     step_inp1 = 1099511627775
#     N_inp2 = 50
#     step_inp2 = 7
#     N_inp3 = 7
#     step_inp3 = 47
#
#     print(fixingTime(fixingTime, N_inp0, step_inp0))
#     print(fixingTime(fixingTime, N_inp1, step_inp1))
#     print(fixingTime(fixingTime, N_inp2, step_inp2))
#     print(fixingTime(fixingTime, N_inp3, step_inp3))