class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        obstacles = set(tuple(obstacle) for obstacle in obstacles)
        max_dist = 0

        for command in commands:
            if command == -1:
                dir_idx = (dir_idx + 1) % len(directions)
                continue
            if command == -2:
                dir_idx = (dir_idx - 1) % len(directions)
                continue

            dx, dy = directions[dir_idx]
            for step in range(command):
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) in obstacles:
                    break

                x, y = new_x, new_y
                max_dist = max(max_dist, x**2 + y**2)
        
        return max_dist

"""
thoughts:
state:
- point (x, y)
- dir facing
- max_dist
- set of obstacles

algorithm:
- go through each command
- if turn (-1 or -2) the just update direction
    - have a list of directions ['N', 'E', 'S', 'W']
    - for -1 just go one to the right in the list
    - for -2 just go one to the left in the list
- if move forward, then move one step at a time
    - for each step before making the step, check if the next point is an obstacle
        - if so stop moving forward
    - after taking each step, check max distance
"""