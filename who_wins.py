me = 0
spouse = 0
dict1 = {
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 5, "spouse": 10 },
  "round3": { "me": 10, "spouse": 10 }}
for i in dict1.values():
    me += (i["me"])
    spouse += (i["spouse"])
                                                    #THIS SOLUTİON WİTH NORMAL METHODS
if me > spouse:
    print("ME!")
elif me < spouse:
    print("SPOUSE!")
else:
    print("DRAW!")    




def determine_who_cursed_the_most(dict1):
    me = 0
    spouse = 0
    for i in dict1.values():
        me += (i["me"])
        spouse += (i["spouse"])                           #THIS SOLUTİON WİTH DEF FUNCTİON
    
    if me > spouse:
        return ("ME!")
    elif me < spouse:
        return ("SPOUSE!")
    else:
        return ("DRAW!") 

print(determine_who_cursed_the_most({
  "round1": { "me": 40, "spouse": 5 },
  "round2": { "me": 9, "spouse": 10 },
  "round3": { "me": 9, "spouse": 10 }}))