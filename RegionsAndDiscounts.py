import pandas as pd
pd.options.display.max_rows=999999
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
data = pd.read_csv("Sample - Superstore.csv", encoding='windows-1252')
new_data = data.dropna()
test_data = new_data.loc[0:9994,["Region","Discount"]]
#print(test_data)

firstP = ""
secondP = ""
thirdP = ""
fourthP = ""

sCount=0
wCount=0
eCount=0
cCount=0

for i in range(9994):
    if (test_data["Region"][i])=="South":
        sCount=(test_data["Discount"][i])+sCount
    if (test_data["Region"][i])=="West":
        wCount=(test_data["Discount"][i])+wCount
    if (test_data["Region"][i])=="East":
        eCount=(test_data["Discount"][i])+eCount
    if (test_data["Region"][i])=="Central":
        cCount=(test_data["Discount"][i])+cCount
    
discList = [sCount,wCount,eCount,cCount]
discList.sort()

regList = []
for i in range (4):
    if discList[i] == sCount:
        regList.append("South")
    if discList[i] == wCount:
        regList.append("West")
    if discList[i] == eCount:
        regList.append("East")
    if discList[i] == cCount:
        regList.append("Central")


print("The",regList[3] , "has given away the most amount of money in discounts!, with a total of", round(discList[3], 2) ,"given away")
print("The",regList[2] , "has given away the second most amount of money in discounts!, with a total of", round(discList[2], 2) ,"given away")
print("The",regList[1] , "has given away the third most amount of money in discounts!, with a total of", round(discList[1], 2) ,"given away")
print("The",regList[0] , "has given away the least amount of money in discounts!, with a total of", round(discList[0], 2) ,"given away")

plt.style.use("fivethirtyeight")
plt.figure(figsize=(11, 6))
plt.title("A Bar Chart to show amounts given away in discounts in each Region")
axis_x=["Central","East","West","South"]
axis_y=[round(discList[3], 2),round(discList[2], 2),round(discList[1], 2),round(discList[0], 2)]
plt.bar(axis_x, axis_y, color="#444444", label="")
plt.show()
plt.figure(figsize=(11, 6))
plt.title("A Pie Chart to show amounts given away in discounts in each Region")
slices=[round(discList[3], 2),round(discList[2], 2),round(discList[1], 2),round(discList[0], 2)]
labels=["Central","East","West","South"]
plt.pie(slices, labels=labels)
plt.show()
