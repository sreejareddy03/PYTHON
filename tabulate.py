from tabulate import tabulate
title=["Name","Age","Dept"]
data=[["Raj",19,"CSE"],
      ["Akash",16,"AIML"],
      ["Meera",34,"CSM"],
      ["Ravi",50,"IT"]]
res=tabulate(data,headers=title,tablefmt="pretty")
print(res)
