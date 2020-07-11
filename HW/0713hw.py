#1

num = int(input())

if (num % 2) == 1:
   print("Weird")
elif 2 <= num < 6:
    print("Not Weird")
elif 6 <= num <21:
    print("Weird")
else:
   print("Not Weird")

#2 성공

line = input()
result = line.replace(" ", "-")
print(result)

#3 작동이 안되는..

your_line = str(input())
your_num = int(input()) 
your_alp = str(input())

a = len(your_line)
if a <= your_num:
    print("The number you gave is too large!")
else :
    print(your_line.replace("your_line[your_num]","your_alp")) 
    