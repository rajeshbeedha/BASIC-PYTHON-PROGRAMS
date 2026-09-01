# --------------------------- Basic Python — 20 Questions--------------------------------
# --Even or Odd--
# Take a number and check whether it is even or odd.
# n=int(input("num:"))
# num=''
# if n%2==0:
#     num="Even"
# else:
#     num="Odd"
# print(f"Given number is {num}")

# --Positive, Negative or Zero--
# Take a number and determine whether it is positive, negative, or zero.
# num=''
# if n>0:
#     num="Positive"
# elif n<0:
#     num="Negative"
# else:
#     num="Zero"
# print(f"Given number is {num}")
# --Largest of Two Numbers--
# ❤️Take two numbers and find the largest.
# n= int(input("Number:"))
# m= int(input("Number:"))
# if n>m:
#     print(n)
# else:
#     print(f"largest:{m}")

# --Take three numbers and find the largest.--
# n= int(input("Number:"))
# m= int(input("Number:"))
# o= int(input("Number:"))
# if n>m:
#     if n>o:
#         print(f"largest:{n}")
#     else:
#         print(f"largest:{o}")
# else:
#     if m>n:
#         print(f"largest:{m}")
#     else:
#         print(f"largest:{o}")

# --Take N and calculate the sum from 1 to N.--
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# --Multiplication Table--
# ❤️Print the multiplication table of a given number from 1 to 10.
# n=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")


# --Factorial--
#❤️ Find the factorial of a given number.
# Example: 5 → 120
# n=int(input("Enter a number:"))
# count=1
# for i in range(1,n+1):
#     count*=i
# print(f"factorial:{count}")

# --Reverse a Number--
# Reverse the digits of a number.
# Example: 12345 → 54321
# n=input("Enter a number:")
# print(n[::-1])

# --Sum of Digits--
# Find the sum of digits of a number.
# Example: 1234 → 10
# num=input("Enter a number:")
# count=0
# for i in num:
#     count+=int(i)
# print(count)

# --Count Digits--
# Count the number of digits in a given number.
# Example: 12345 → 5
# num=input("Enter a number:")
# count=0
# for i in num:
#     count+=1
# print(count)

# ------- Slightly More Practice---------
# --- Palindrome Number---
# Check whether a number is a palindrome.
# Example: 121 → Palindrome
# n=input("enter a number:")
# if n==n[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")
# Prime Number
# Check whether a number is prime.
# Example: 7 → Prime
# count=0
# n=int(input())
# for i in range(1,n):
#     if i%1==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not a prime")
# ---Prime Numbers in a Range---
#❤️Print all prime numbers between 1 and 100.
# min=1
# max=100
# for i in range(min,max+1):
#     if i>1:
#         for j in range(2,i):
#             if(i%j==0):
#                 break
#         else:
#             print(i,end=" ")

# ---Fibonacci Series---
# Print the first N terms of the Fibonacci series.
# Example: 0 1 1 2 3 5 8...
# n=int(input("enter value:"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)
# ---Armstrong Number---
# Check whether a number is an Armstrong number.
# # Example: 153 → Armstrong
# n=int(input())
# arm=n
# count=0
# while n>0:
#     digit=n%10
#     count=count+digit**3
#     n=n//10
# if count==arm:
#     print("Armstrong")
# else:
#     print("Not an armstrong")
# --
# num = int(input("Enter a number: "))
# original = num
# total = 0
# while num > 0:
#     digit = num % 10
#     total = total + digit ** 3
#     num = num // 10
# if total == original:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")
    
# ---Reverse a String---
# Reverse a given string.
# Example: "Python" → "nohtyP"
# n=input()
# print(n[::-1])
# ---Count Vowels---
# Count the number of vowels in a string.
# Example: "education" → 5
# n=input().lower()
# b=("a,e,i,o.u")
# count=0
# for i in n:
#     if i in b:
#         count+=1
# print(f"{n}:{count}")

# ---Palindrome String---
# Check whether a string is a palindrome.
# Example: "madam" → Palindrome
# n=input()
# if n==n[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#--- Largest Number in a List---
# Given:
# numbers = [10, 25, 5, 40, 15]
# Find the largest number without using max().
# numbers = [10, 25, 5, 40, 15]
# largest=0
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)

# ----Second Largest Number ⭐----
# # Given:
# numbers = [10, 25, 5, 40, 15,35]
# largest=0
# second=0
# for i in numbers:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest:", second)



