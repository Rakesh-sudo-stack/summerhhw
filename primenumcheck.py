try:
    n = int(input("Enter any number: "))
    flag = True
    def checkPrime(n):
        for i in range(2,n):
            if not n%i:
                return False
            if i==n-1:
                return True
        return True
    flag = False if n<=1 else checkPrime(n)
    print("It is a prime number" if flag else "It is not a prime number")
except Exception as e:
    print("Invalid input")
