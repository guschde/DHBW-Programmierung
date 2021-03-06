#encoding=utf-8
#Schreiben Sie die Funktion maximum(a,b), die den größeren der beiden Werte zurück liefert.
def maximum(a,b):
    if(a>b):
        return a
    else:
        return b
#Schreiben Sie eine Funktion square(x) die das Quadrat von x berechnet
def square(x):
    return x**2
#Schreiben Sie eine Funktion even(n), die True zurücklifert, wenn n eine gerade Zahl ist. Verwenden Sie dazu keine if-Anweisung.
def even(n):
    return bool(n%2==0)
print(even(10))

#Euklid'schen Algorithmus zur Berechnung des größten gemeinsamen Teilers zweier Zahlen
def ggt(a, b):
    if a == 0:
        return b
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print(ggt(44, 12))
#Schreiben Sie eine Funktion mean, die den Mittelwert der Elemente einer als Parameter übergebenen Liste berechnet und zurückgibt. Gehen Sie dazu die Liste elementweise durch und addieren die Werte in einer Variable auf. Teilen Sie diesen Wert dann durch die Anzahl der Elemente in der Liste.
def mean(l):
    Summe = 0
    for e in l:
        Summe = Summe + e
    return (Summe/len(l))

l = [1,5,8,4,2]
print(mean(l))
#Die Fakultät einer natürlichen Zahl n ist definiert als
def fakultaet(n):
    if (n == 0):
        return 1
    else:
        return n*fakultaet(n-1)
print(fakultaet(5))
#Fakultät ohne Rekursion
def fak(n):
    summe = n
    while n > 1:
       summe = summe * (n-1)
       n -= 1
    return summe
print(fak(5))

#Oder So:
def fakultaet(n):
    summe = 1
    for i in range(n, 1, -1):
        summe *= i
    return summe


print(fakultaet(6))



#Schreiben Sie ein Programm, das diese Folge berechnet und dabei die (rekursive) Funktion fib(n) implementiert.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(2))