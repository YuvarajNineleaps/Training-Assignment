"""Sorting a json file content using merge sort that has name, id and marks.
Input : File Name , A json file that has name, marks and id attribute to be sorted.
Output: Sorted json by selected option such as name, marks, id.
"""

import sys
import json

class JsonSort:
    """Sorting an list of  dict using merge sort."""
    def merge_sort(self, data, low, high, option):
        """Dividing and sorting the list using merge sort.

        :param data: list, list of dict
        :param low: int, lower index
        :param high: int, higher index
        :param option: str, choice of name, marks, id to be sorted
        """
        if low < high:
            mid = (low + high) / 2
            self.merge_sort(data, low, mid, option)
            self.merge_sort(data, mid + 1, high, option)
            self.merge(data, low, mid, mid + 1, high, option)

    def merge(self, data, i1, j1, i2, j2, option):
        """Sorting and merging the list by option.

        :param data: list, list of dict
        :param i1: int, lower index lower list
        :param j1: int, higher index lower list
        :param i2: int, lower index higher list
        :param j2: int, higher index higher list
        :param option: str, choice of name, marks, id to be sorted
        """
        i = i1
        j = i2
        temp = []
        while (i <= j1) and (j <= j2):
            if data[i].get(option) < data[j].get(option):
                temp.append(data[i])
                i += 1
            else:
                temp.append(data[j])
                j += 1
        while i <= j1:
            temp.append(data[i])
            i += 1
        while j <= j2:
            temp.append(data[j])
            j += 1
        k = 0
        for i in range(i1, j2+1):
            data[i] = temp[k]
            k += 1

# Check file name in command line argument.
if len(sys.argv) < 2:
    print "Usage : json_sort.py <json file>"
    exit(1)

sort = JsonSort()

#  Get json file name from command line.
json_file = sys.argv[1]

print "1. Name sort\n2. Marks sort\n3. ID sort\n4. Exit"
print "-----------------------"
option = {1: "name", 2: "marks", 3: "id", 4: 0}
select = int(raw_input("Input choice :"))
while option[select]:
    with open(json_file) as data_file:
        data = json.load(data_file)
    low = 0
    high = len(data) - 1

    sort.merge_sort(data, low, high, option[select])
    print data

    select = int(raw_input("Input choice :"))

