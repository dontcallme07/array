scores = input("Enter scores separated by spaces: ")

scores = [float(score) for score in scores.split()]

print("Scores:", scores)
print("Total:", sum(scores))
print("Average:", sum(scores) / len(scores))