def pallin(num):
    org=num
    rev=num[::-1]
    if org==rev:
        print("yes pallindrome")
    else:
        print("nott palindrome")  
k=input("enter the number")
pallin(k)
      