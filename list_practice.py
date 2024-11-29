# # # hall= 11.25
# # # liv= 20
# # # bath = 35

# # # all_area=[hall,liv,bath]
# # # print(all_area)
# # # print(sum(all_area))
# # # print(max(all_area))
# # # print(min(all_area))
# # # print(len(all_area))

# # n=int(input("Enter the number of elements: "))
# # list1=[]
# # for i in range(0,n):
# #     # ele=int(input('de magia: '))
# #     ele=i
# #     list1.append(ele)   # adding the element
# # print(list1)    
# # print(sum(list1))           
# # print(max(list1))       
# # print(min(list1))   
# # print(len(list1))


# a=[1,2,3]
# b=[4,5,6]
# c=a
# a.append(b)
# print(a)
# # c.extend(b)
# # print(c)
# # a.pop(-2)
# # print(a)
# a=["alu","potol","lau","alu"]

# b=a.copy()
# print(b is a)

# TwoDList = [[1,2,3],[4,5,6],[7,8,9]]
# rowsums = []



height=[1.73,1.68,1.71,1.89,1.79]   
weight=[65.4,59.2,63.6,88.4,68.7]
bmi=[]

for i in range(len(height)):
    bmi.append(round((weight[i]/height[i]**2),2))

print((bmi))
