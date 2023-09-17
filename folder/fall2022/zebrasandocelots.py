from readline import append_history_file


list = []
for i in range(int(input())):
    list.append(1) if input() == 'Z' else list.append(0)

