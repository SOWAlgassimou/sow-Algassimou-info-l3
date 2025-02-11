def fibonacci_sup(n):
    F1, F2 = 1, 1
    while F2 <= n:
        F1, F2 = F2, F1 + F2
    return F2
print("Premier nombre de fibonacci supérieur à 75:", fibonacci_sup(75))
print("Premier nombre de fibonacci supérieur à 50:", fibonacci_sup(50))
print("Premier nombre de fibonacci supérieur à 100:", fibonacci_sup(100))