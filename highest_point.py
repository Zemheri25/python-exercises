def function_of_team(dict1):
    dict1 = {}
    name = input("Please enter your team : ")
    wins = int(input("Please enter the wins rate : "))
    loss = int(input("Please enter losses rate of team : "))
    draws = int(input("Please enter the draws of team : "))
    scored = int(input("Please enter the scores of the team : "))
    conceded = int(input("Please enter the concede of the team : "))

    dict1["name"] = name
    dict1["wins"] = wins
    dict1["draws"] = draws
    dict1["scored"] = scored
    dict1["loss"] = loss
    dict1["conceded"] = conceded

    return dict1


a = function_of_team(dict1={})
b = function_of_team(dict1={})
c = function_of_team(dict1={})

dict2 = {}
champions = [a, b, c]
for i in champions:
    count  = 0
    count = count + i["wins"]*3 + i["loss"]*0 + i["draws"] * 1
    dict2[i["name"]] = count

a = (max(dict2, key=dict2.get))
print(a)