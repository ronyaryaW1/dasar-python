# 1. cabang_loop dengan while
# a = 1
# while a < 5:
#     b = 0 
#     while b < a:
#         print("$", end='')
#         b = b + 1
#     print()
#     a = a+1

# 2. kita buat perkalian dengan for 
for a in range(1,4):
    for b in range(1,4):
        c = a*b
        print(c, end=" ")
    print()