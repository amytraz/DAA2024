import numpy as np
import math

class AssignmentProblem:
    def __init__(self, cost_matrix):
        self.cost_matrix = cost_matrix
        self.n = len(cost_matrix)
        self.final_assignment = [None] * self.n
        self.min_cost = float('inf')

    def get_lower_bound(self, assignment):
        """Calculate the lower bound for the current assignment."""
        row_cover = [False] * self.n
        col_cover = [False] * self.n
        lb = 0

        for i in range(len(assignment)):
            if assignment[i] is not None:
                row_cover[i] = True
                lb += self.cost_matrix[i][assignment[i]]

        for i in range(self.n):
            if not row_cover[i]:
                lb += min(self.cost_matrix[i])

        return lb

    def branch_and_bound(self, assignment, row):
        """Recursive function to explore assignments."""
        if row == self.n:
            current_cost = self.get_lower_bound(assignment)
            if current_cost < self.min_cost:
                self.min_cost = current_cost
                self.final_assignment = assignment.copy()
            return

        for col in range(self.n):
            if col not in assignment:
                assignment[row] = col
                bound = self.get_lower_bound(assignment)
                if bound < self.min_cost:
                    self.branch_and_bound(assignment, row + 1)
                assignment[row] = None  # Backtrack

    def solve(self):
        assignment = [None] * self.n
        self.branch_and_bound(assignment, 0)
        return self.final_assignment, self.min_cost


def get_cost_matrix():
    n = int(input("Enter the number of students (and clubs): "))
    cost_matrix = []

    print("Enter the cost matrix row by row (space-separated):")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != n:
            raise ValueError("Each row must have exactly N values.")
        cost_matrix.append(row)

    return cost_matrix


if __name__ == "__main__":
    cost_matrix = get_cost_matrix()
    problem = AssignmentProblem(cost_matrix)
    assignment, min_cost = problem.solve()

    print("Optimal Assignment:", assignment)
    print("Minimum Cost:", min_cost)
