class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        win_counts, loss_counts = {}, {}
        for winner, loser in matches:
            win_counts[winner] = win_counts.get(winner, 0) + 1
            loss_counts[loser] = loss_counts.get(loser, 0) + 1

        for player, count in win_counts.items():
            if player not in loss_counts:
                ans[0].append(player)
        for player, count in loss_counts.items():
            if count == 1:
                ans[1].append(player)

        ans[0].sort()
        ans[1].sort()

        return ans

"""
INTIAL THOUGHTS:
- map of player to win-loss record
"""