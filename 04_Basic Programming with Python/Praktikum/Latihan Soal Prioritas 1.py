# SOAL PRIORITAS 1

# ------------------------ NO 1 ---------------------------
p = 2
l = 5

p *= l

if p % 2 == 0:
    print("even rectangle")
else:
    print("odd rectangle")


# ------------------------ NO 2 ---------------------------
    
r = 21
phi = 3.14

print(4/3*phi*r**3)


# ------------------------ NO 3 ---------------------------

class Solution(object):
    def numbers(self, n):
        result = []
        for x in range(1, n + 1):
            if x % 3 and x % 5 == 0: 
                result.append("buzz")
            elif x % 3 == 0:
                result.append(x**2)
            elif x % 5 == 0:
                result.append(x**3)
            else:
                result.append(x)  
        return result
ob1 = Solution()
print(ob1.numbers(100))

