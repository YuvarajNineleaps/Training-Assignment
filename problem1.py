class SeatArrangement:
    """Class to get seat arrangements"""
    def arrange(self, employee_reporting_detail, n):
        """ Arraanges the hierarchy.

        :param employee_reporting_detail: list, contains employee details
        :param n: no. of employees
        """
        flag = 1
        for i in range(n):
            h_employee = employee_reporting_detail[i][1]
            for j in range(1, n):
                l_employee = employee_reporting_detail[j][0]
                if h_employee == l_employee:
                    temp = employee_reporting_detail[flag]
                    employee_reporting_detail[flag] = employee_reporting_detail[j]
                    employee_reporting_detail[j] = temp
                    flag += 1

seat_arrange = SeatArrangement()
n = int(raw_input())
# employee and their reporting manager
# employee_reporting detail = [[reporting_manager][employee]]
employee_reporting_detail = [[0, 1]]

reporting_manager = raw_input()
reporting_manager_list = reporting_manager.split(" ")
employee_id = 2

# Create list with reporting manager and employee id
for i in reporting_manager_list:
    employee = [int(i), employee_id]
    employee_reporting_detail.append(employee)
    employee_id += 1

seat_arrange.arrange(employee_reporting_detail, n)

# To print row - wise
row = []
for i in range(len(employee_reporting_detail)):
    row.append(employee_reporting_detail[i][1])
    if i%5 == 4:
        print row
        row = []
print row



