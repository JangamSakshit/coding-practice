# Python


# Introduction
# It was created by Guido van Rossum, and released in 1991.


# Python Lists
# Ordered, allow duplicates, changable
# use [] brackets


# Level 1: Basic List Practice (Easy)
# 1. Print all elements of a list.
nums = [10, 20, 30, 40]
for lp in nums:
    print(lp)


# 2. Find the sum of all numbers in a list.
l1 = [5,4,3]
total = 0

for a in l1:
    total += a

print("Sum is:- ",total)


# 3. Find the largest number.
l2 = [3,9,2,7,18]
max_val = l2[0]

for b in l2:
    if b > max_val:
        max_val = b

print("Largest Number is:-", max_val)


# 4. Find the smallest number.
l3 = [3,9,7,18]
min_val = l3[0]

for c in l3:
    if min_val > c:
        min_val = c

print("Smallest number:-", min_val)


# 5. Count how many even numbers are in the list.
l4 = [2,5,8,9,10]
count = 0

for d in l4:
    if d % 2 == 0:
        count += 1

print("Total even number in l2 is:-", count)


# 6. Count how many odd numbers are in the list.
l5 = [2,5,8,9,10]
count = 0

for e in l5:
    if e % 2 == 1:
        count += 1

print("Total odd number in l5 is:-", count)

