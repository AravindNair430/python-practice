# print("Hello Sir. HAIJ at your service.")

# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("//____|")

# character_name="Jojo"
# character_age="30"
# print("There was a man named "+character_name+",")
# print("He was "+character_age+" years old")

# WORKING WITH STRINGS

# name="Joel"
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# print(name.upper().isupper())
# print(name[2])
# print(name.index("o"))
# print(name.replace("o", "m"))

# WORKING WITH  NUMBERS
# from  math import *
# print(2)
# print(2.23)
# print(2+78)
# print(2*7+5)
# print(2*(7+5))
# num=-5
# print(num)
# print(abs(num))
# print(pow(2,3))
# print(max(4,6))
# print(min(4,6))
# print(round(3.2))
# print(round(3.7))
# print(floor(3.7))
# print(ceil(3.2))
# print(sqrt(3.7))

#  INPUT FROM USER
#
#
# name=input("Enter your name: ")
# print("Hello Mr."+name)


# num1=input("Enter a number: ")
# num2=input("Enter another number: ")
#
# result=float(num1)+float(num2)
# print(result)

#LISTS

# friends=["kunal","Malavika","Vishal","Tony Stark","Steve Rogers"]
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])

#LIST FUNCTIONS

# friends=["kunal","Malavika","Vishal","Tony Stark","Steve Rogers"]
# lucky_numbers=[1,2,3,4,5,6,7,8,9,10]
#
# friends.append(lucky_numbers)
# friends.append(2)
# friends.insert(1,"John Wick")
# friends.remove("John Wick")
# friends2=friends.copy()
# lucky_numbers.reverse()
# print (friends)
# print(lucky_numbers)
# print(friends2)


#TUPLES

# coordinates=(2,3)
# coordinates[0]=4 THIS CODDE WILL NOT WORK
# print(coordinates[0])

#FUNCTIONS

# def joel():
#     print("Hi there, miss me?")
#
# joel()
#
# def cube(num):
#     return num*num*num
#
# print(cube(4))


#IF ELSE ELIF

# is_genius = False
# is_high_score = False
#
#
# if is_genius and is_high_score :
#     print("Congratulations, you just survived the bashing from the teachers")
# elif is_genius and not(is_high_score):
#     print("You're doing well. Don't listen to others.")
# elif not(is_genius) and is_high_score:
#     print("Get the hell out of my sight. Pathetic Losers")
# elif not(is_genius) and not(is_high_score):
#     print("Go Look for something else. This is not your cup of tea.")
#


#DICTIONARY

# monthconversions = {
#     "Sun": "Sunday",
#     "Mon": "Monday",
#     "Tue": "Tuesday",
#     "Wed": "Wednesday",
#     "Thurs": "Thursday",
#     "Fri": "Friday",
#     "Sat": "Saturday"
# }
#
# print(monthconversions["Wed"])
# print(monthconversions.get("Wed", "not a valid key"))


#WHILE

# i=1
# while i<=10:
#     print(i)
#     i=i+1


#NUMPY

import numpy as np

# L = [1, 2, 3]
# A = np.array([1, 2, 3])
#
# for e in L:
#     print (e)
#
# for e in A:
#     print (e)
#
# print(A+A)
# print(2*A)
# print(2*L)
# print(A**2)
# print(np.sqrt(A))

# a=np.array([1, 2])
# b=np.array([2, 1])
#
# dot=0
#
# for e,f in zip(a,b):
#     dot+=e*f
#
# print(dot)
# print(a*b)
# print(np.sum(a*b))
# print(np.dot(a,b))
#
# amag=np.sqrt(np.sum(a*a))
# print(amag)
#
# print(np.linalg.norm(a))
#
# cosangle= np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
# print(cosangle)
#
# angle=np.arccos(cosangle)
# print(angle)

# VECTORS AND MATRICES

# M= np.array([[1,2],[3,4]])
# L=[[1,2],[3,4]]
#
# print(L[0][0])
# print(M)
#
# print(M[0,0])
# M2=np.matrix(M)
# print(M2)

# Z=np.zeros((10,10))
# Z=np.ones(10)
# print (Z)
# z=np.random.random((10,10))
# print(z)
# G=np.random.randn(10,10)
# print(G)
# print(G.mean())
# print(G.var())

# MORE MATRIX OPERATIONS

# A=np.array([[1, 2],[3, 4]])
# Ainv=np.linalg.inv(A)
# print (Ainv)
#
# print(Ainv.dot(A))
# print(np.linalg.det(A))
# print(np.diag(A))
# print(np.diag([1, 2]))


#SOLVING A LINEAR EQUATION

# A=np.array([[1, 2],[3, 4]])
# B=np.array([1,2])
# # x=np.linalg.inv(A).dot(B)
# y=np.linalg.solve(A,B)
# print(y)


#PANDAS

X = []

# for line in open("data_2d.csv"):
#     row = line.split(',')
#     sample = map(float, row)
#     X.append(sample)
#
# print (X)
#
# X=np.array(X)
#
# print(X)

import pandas as pd

# X=pd.read_csv("data_2d.csv", header=None)
# # print(type(X))
# #
# #
# # print(X.head(10))
#
#
# # M=X.as_matrix(X)
# print(X[0])
# print(X.iloc[0])
# print(X[[0, 2]])

#DATAFRAMES AND COLUMN FRAMES


# df=pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
#
# df['ones'] = 1
#
# df.columns = ["month", "passengers"]


#JOINS

# t1=pd.read_csv("table1.csv" )
# t2=pd.read_csv("table2.csv" )
# print(t1)
# print(t2)
#
# m=pd.merge(t1,t2,on="user_id")
# print(m)
# print(t1.merge(t2, on="user_id"))


#MATPLOTLIB

import matplotlib.pyplot as plt
#
# x=np.linspace(0,10,10)
# y=np.sin(x)
# plt.plot(x,y)
# plt.xlabel("TIME")
# plt.ylabel("Some function of time")
# plt.title("My cool chart")
# plt.show()


#SCATTERPLOT

# A = pd.read_csv("data_1d.csv", header=None).as_matrix()
# x=A[:,0]
# y=A[:,1]
# # plt.scatter(x,y)
# # plt.show()
# #
# #
# # x_line=np.linspace(0,100,100)
# # y_line=2*x_line+1
# #
# # plt.scatter(x,y)
# # plt.plot(x_line,y_line)
# # plt.show()
#
# plt.hist(x,  bins=20)
# plt.show()


#SCIPY

from scipy.stats import norm

print(norm.pdf(0))
print(norm.pdf(0,loc=5, scale=10))
