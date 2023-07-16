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
