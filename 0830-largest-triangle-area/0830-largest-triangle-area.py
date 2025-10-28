class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def distance(p1, p2) -> float:
            return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5

        def area(p1, p2, p3) -> float:
            a = distance(p1, p2)
            b = distance(p1, p3)
            c = distance(p2, p3)
            s = (a + b + c) / 2
            return (s * abs(s - a) * abs(s - b) * abs(s - c)) ** 0.5

        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, area(points[i], points[j], points[k]))

        return res
