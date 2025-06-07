n = int(input("Enter the number of rows: "))

# Lower Triangular Pattern
print("Below is the Lower triangular pattern with n rows")
for i in range(1, n + 1):
    print("* " * i)

# Upper Triangular Pattern
print("Below is the upper triangular pattern with n rows")
for i in range(n, 0, -1):
    print("* " * i)

# Pyramid Pattern
print("Below is the pyramid pattern with n rows")
#pyramid can be considered as concatenation of spaces and stars
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
