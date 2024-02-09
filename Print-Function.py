if __name__ == '__main__':
    n = int(input(""))
    
    # Ensure n is positive
    if n > 0:
        # Loop to print the pattern
        for i in range(1, n + 1):
            # Print the numbers without spaces or string methods
            print(i, end="")