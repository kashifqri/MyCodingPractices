import pandas as pd
# x=[1,2,3,4,5,6,7,8]
# x={"name":["python","c","c++","java"],"popular":[1,4,3,2]}
# var=pd.Series(12,index=[1,2,3,4,5,6])
# print(var)
# var=pd.DataFrame({"a":[1,2,3,4,5],"s":[6,7,8,9,1],"d":[1,2,3,4,5]})
# var.insert(2,"python",[12,3,4,5,6]) use for insert data
# var.pop("a") use for comment
# # var=pd.DataFrame(x)
# # x["c"]=x["a"]+x["s"]+x["d"]         operator use
# print(var)

CSV_1=pd.read_csv("C:\\Users\\basit\\Desktop\\test.csv.csv")
print(CSV_1)
CSV_1.loc[1,"vote_average"]=2.345
print(CSV_1)