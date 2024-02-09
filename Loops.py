if __name__ == '__main__':
    n = int(input(""))
    
    # Ensure n is non-negative
    if n >= 0:
        # Print the squares of non-negative integers less than n
        for i in range(n):
            print(i ** 2)
    else:
        print("Please enter a non-negative integer.")
