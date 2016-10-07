"""Ranks employee based on the ranking.
Input : n: int, no of employees
        m: int, no of ranked to be displayed and
        employee_detail: str, employee name designation and rank
Output: m employess based on ranking
"""
class Ranking:
    """Class for displaying employess by rank."""
    def max_heapify(self, employee_detail_list, i):
        """ Heapify employees by ranking.

        :param employee_detail_list: list, employees detail list
        :param i: int, no of employees minus 1
        """
        index = i
        while (employee_detail_list[index][2] > employee_detail_list[((index)/2)][2] and index > 0):
            tmp = employee_detail_list[index]
            employee_detail_list[index] = employee_detail_list[index/2]
            employee_detail_list[index/2] = tmp
            index = (index/2)

rank = Ranking()
employee_detail_list = []
n = int(raw_input())
m = int(raw_input())

# Get employee Details
for i in range(n):
    employee_detail = raw_input("Input :")
    employee_detail = employee_detail.split(" ")
    employee_detail_list.append(employee_detail)
    rank.max_heapify(employee_detail_list, i)

# To display m employees by ranking
for i in range(m):
    print " ".join(employee_detail_list[i])
