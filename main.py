import csv

rows = []
mr = {
    "rank": 0,
    "matches": 0
} 
qp = {
    "rank": 0,
    "matches": 0
}

with open('GM_players_statistics.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            if len(row[17].split(".")) > 0 and row[20].split(".")[0] and row[21].split(".")[0] and row[22].split(".")[0]:
                rows.append({
                    "rank" : int(row[17].split(".")[0]),
                    "matches" : int(row[20].split(".")[0]) + int(row[21].split(".")[0])  + int(row[22].split(".")[0]) 
                })
        except ValueError:
            pass
        
bestranks = sorted(rows, key=lambda rank: rank["rank"], reverse = True)
mostplayed = sorted(rows, key=lambda matches: matches["matches"], reverse = True)

for i in range(100):
    mr["rank"] += bestranks[i]["rank"]
    mr["matches"] += bestranks[i]["matches"]
    qp["rank"] += mostplayed[i]["rank"]
    qp["matches"] += mostplayed[i]["matches"]
    
mr["rank"] = mr["rank"] / 100
mr["matches"] = mr["matches"] / 100
qp["rank"] = qp["rank"] / 100
qp["matches"] = qp["matches"] / 100

print(mr)
print(qp)