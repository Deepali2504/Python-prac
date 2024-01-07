# WAP to create a pyramid of the character ‘*’ and a reverse pyramid
#     * 
#    *** 
#   ***** 
#  ******* 
# *********
                            # ********* 
                            #  ******* 
                            #   ***** 
                            #    *** 
                            #     * 

rows = int(input("Enter the number of rows: "))
# Upward Pyramid
print("Upward Pyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i-1))

# Downward Pyramid
print("\nDownward Pyramid:")
for i in range(rows,0,-1):
    print(" "*(rows-i)+ "*"*(2*i-1))