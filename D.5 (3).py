def count_perfect_squares(n):
    count = 0
    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            if j*j == i:
                count += 1
                break
            j += 1
    return count

n = int(input("Enter a number: "))
print("Number of perfect squares between 1 and", n, ":", count_perfect_squares(n)) 

