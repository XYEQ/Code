# Input works as follows:
# First line: Number of cases
# Each case will include
#    - The first line of each case will contain either "ENCRYPT" or "DECRYPT"
#    - The second line of each case will contain the cipher key which will be 26 characters which map in order to the standard English alphabet
#    - The third line of each case will contain a positive integer N representing the number of messages to follow
#    - N lines of each case will contain a message which needs to be either encrypted or decrypted depending on what is inputted on the first line

import string

inputs = int(input())

for i in range(inputs):
    command = input()
    if command == "ENCRYPT":
        key = dict(zip(string.ascii_lowercase,input()))
    else:
        key = dict(zip(input(),string.ascii_lowercase))

    messages = []
    messages_num = int(input())

    for k in range(messages_num):
        messages.append(input())

    for g in range(messages_num):
        text = ""
        for n in messages[g]:
            if n.isupper():
                text += key[n.lower()].upper()
            elif n == " ":
                text += n
            else:
                text += key[n]

        print(text)
