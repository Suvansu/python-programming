# print("hello")
# print("trying new thing")

# name = "suvansu paudel"
# a = 10
# b = 20
# c = 30
# total = a + b + c 

# print("Hello my name is" + name + "my first variable is " + str(a) + " my second variable is" , b, "my third variable is" , c, "when I add them together I get" , total)


# x = 50

# y = 30

# print("addition: " + str(x + y))

# print("subtraction: " + str(x - y))

# print("multiplication: " + str(x * y))

# print("division: " + str(x / y))

# print("modulus: " + str(x % y))

# print("exponent: " + str(x** y))

# print("floor division: " + str(x // y))


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\suvan\Documents\sem 1\Big Data Fund\bankinfo.csv", sep=';')


#print(df.head)

print(df.describe())

df['age'].hist(bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()