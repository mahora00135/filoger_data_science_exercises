from tabulate import tabulate
txt = (input('Pleas Enter English text : ')).replace(" ", "")
print(tabulate({i: txt.count(i) for i in set(txt)}.items(), headers = ["Name", "Frequency"], tablefmt = "pretty"))

