a=b=c=d=e=f=i=n=0
n = int(input("Number of student : "))
while i < n :
  score = int(input("score of student : "))
  if score >= 90 and score <= 100 :a += 1
  elif score >= 80 and score <= 89 :b += 1
  elif score >= 70 and score <= 79 :c += 1
  elif score >= 60 and score <= 69 :d += 1
  elif score >= 50 and score <= 59 :e += 1
  elif score >= 0 and score <= 49 :f += 1
  else :
    print("---->ERROR<----")
    i -= 1
  i += 1
print("90-100 :",end = " ")
for score in range(0,a):print("*",end = "")
print("\n80-89 :",end = " ")
for score in range(0,b):print("*",end = "")
print("\n70-79 :",end = " ")
for score in range(0,c):print("*",end = "")
print("\n60-69 :",end = " ")
for score in range(0,d):print("*",end = "")
print("\n50-59 :",end = " ")
for score in range(0,e):print("*",end = "")
print("\n0-49 :",end = " ")
for score in range(0,f):print("*",end = "")