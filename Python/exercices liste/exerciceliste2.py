plan = [["Inès", "Malo", "Léa"],["Yanis", "Zoé", "Enzo"],["Lina", "Noah", "Jade"]]
print(plan[0][1])
print(plan[2][1])
plan[1][1],plan[2][1] = plan[2][1],plan[1][1]
plan[0][2] = ""
plan.append(["Tom","Sam",""])
assert plan == [["Inès", "Malo", ""],
                ["Yanis", "Noah", "Enzo"],
                ["Lina", "Zoé", "Jade"],
                ["Tom", "Sam", ""]]
