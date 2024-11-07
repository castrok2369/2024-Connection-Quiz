import csv

file = open("connections_quiz.csv", "r")
all_connections = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_connections.pop(0)

# get the first 50 rows (used to develop connection
# buttons for play GUI)
print(all_connections[:50])

print("Length: {}".format(len(all_connections)))