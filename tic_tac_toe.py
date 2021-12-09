tictoc = [
  ["X", "O", "O"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]

result = "Draw"

vertical = list(map(lambda *x: [*x] , *tictoc))
for i in range(len(tictoc)):
    if len(set(tictoc[i])) == 1 and tictoc[i][0] != "E":
        result = tictoc[i][0]
        break
    elif len(set(vertical[i])) == 1 and vertical[i][0] != "E":
        result = vertical[i][0]
        break

if tictoc[0][0] == tictoc[1][1] == tictoc[2][2] and tictoc[0][0] != "E":
    result = tictoc[0][0]
elif tictoc[0][2] == tictoc[1][1] == tictoc[2][0] and tictoc [1][1] != "E":
    result = tictoc[0][2]

print(result)  