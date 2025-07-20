import re

order = input("Enter number orders to arrange values:")

values =input("Enter values: ").split(',')
#order = input("Enter number orders to arrange values:")
#stripped = re.sub(r"[{}]", "", order)

cleaned = re.sub(r"[{}]", "", order)
#stripped = [int(i) for i in order.strip()]

#reordered = [values[i] for i in order]
indices = [int(i) for i in cleaned]
reordered = [values[i] for i in indices]

print("Reordered: ", ' '.join(reordered))
