class IslandsCounter:
    def __init__(self, matrix):
        self._matrix = matrix

    def count_islands(self):
        if self._matrix is None or not any(self._matrix):
            return 0

        islands = 0
        matrix = [m[:] for m in self._matrix]
        max_i = len(matrix)
        max_j = len(matrix[0])

        for (i, row) in enumerate(matrix):
            for (j, col) in enumerate(row):
                if col == 1:
                    islands += 1
                    self._walk_through_island_parts(matrix, i, j, max_i, max_j)

        return islands

    def _walk_through_island_parts(self, matrix, i, j, max_i, max_j):
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            matrix[i][j] = -1

            pos_inc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for i_inc, j_inc in pos_inc:
                new_i = i + i_inc
                new_j = j + j_inc
                if (new_i >= 0 and new_i < max_i and
                    new_j >= 0 and new_j < max_j and
                    matrix[new_i][new_j] == 1):
                    queue.append((new_i, new_j))
