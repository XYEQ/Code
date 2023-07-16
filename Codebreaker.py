# Input works as follows
# First line: number of cases to process
# Each case will contain
#    - A line containing a positive integer, X, indicating the number of lines of text to be provided.
#    - X lines, containing text to be analyzed.

import string

inputs = int(input())

for i in range(inputs):
    num_strings = int(input())
    strings = []
    for k in range(num_strings):
        strings.append(input())

    count_alpha = dict.fromkeys(string.ascii_lowercase,0)

    for m in strings:
        for n in m:
            if not n.isalpha():
                continue
            count_alpha[n.lower()] += 1


    len_str = sum(count_alpha.values())

    for l in string.ascii_lowercase:
        count_alpha[l] = str(round((count_alpha[l]/len_str) * 100,2)).ljust(4,"0")

        if count_alpha[l][1] != ".":
            count_alpha[l] = count_alpha[l].ljust(5,"0")
    
    for m in string.ascii_lowercase:
        print(m.upper() + ": " + count_alpha[m] + "%")

