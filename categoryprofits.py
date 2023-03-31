import pandas as pd
pd.options.display.max_rows=999999
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
data = pd.read_csv("Sample - Superstore.csv", encoding='windows-1252')
new_data = data.dropna()
test_data = new_data.loc[0:9994,["Category","Profit"]]
#print(test_data)
fcount=0
ocount=0
tcount=0
for i in range(9994):
    if (test_data["Category"][i])=="Furniture":
        fcount=(test_data["Profit"][i])+fcount
    if (test_data["Category"][i])=="Office Supplies":
        ocount=(test_data["Profit"][i])+ocount
    if (test_data["Category"][i])=="Technology":
        tcount=(test_data["Profit"][i])+tcount


profList = [fcount,ocount,tcount]
profList.sort()
catList = []
for i in range (3):
    if profList[i] == fcount:
        catList.append("Furniture")
    if profList[i] == ocount:
        catList.append("Office Supplies")
    if profList[i] == tcount:
        catList.append("Technology")


print("The",catList[2] , "has given away the most amount of money in discounts!, with a total of", round(profList[2], 2) ,"given away")
print("The",catList[1] , "has given away the second most amount of money in discounts!, with a total of", round(profList[1], 2) ,"given away")
print("The",catList[0] , "has given away the third most amount of money in discounts!, with a total of", round(profList[0], 2) ,"given away")

plt.style.use("fivethirtyeight")
plt.figure(figsize=(11, 6))
plt.title("A Bar Chart to show  the profits of different categories of items")
axis_x=["Furniture","Office Supplies","Technology"]
axis_y=[round(profList[2], 2),round(profList[1], 2),round(profList[0], 2)]
plt.bar(axis_x, axis_y, color="#444444", label="")
plt.show()
plt.figure(figsize=(11, 6))
plt.title("A Pie Chart to show the profits of different categories of items")
slices=[round(profList[2], 2),round(profList[1], 2),round(profList[0], 2)]
labels=["Furniture","Office Supplies","Technology"]
plt.pie(slices, labels=labels)
plt.show()