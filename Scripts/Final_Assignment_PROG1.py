# Final Assignment PROG1: Basics & statements

# vraagt de product prijs op
Productprijs = int(input("Product prijs(in centen): "))
# vraagt de prijs van ingegeven munten op
Betaalbedrag = int(input("je betaald het bedrag(in centen): "))

# rekent uit wat terug gegeven moet worden
A = Betaalbedrag - Productprijs

# kijkt hoe vaak 50 past in het terug te geven bedrag
B = A // 50
# haalt zo vaak mogelijk 50 eraf en de output is wat over blijft
C = A % 50

D = C // 20
E = C % 20

F = E // 10
G = E % 10

H = G // 5
I = G % 5

J = I // 2
K = I % 2

L = K // 1
M = K % 1
# print de aantallen uit
print("aantal munten van 50 eurocent is: " + str(B))
print("aantal munten van 20 eurocent is: " + str(D))
print("aantal munten van 10 eurocent is: " + str(F))
print("aantal munten van 5 eurocent is: " + str(H))
print("aantal munten van 2 eurocent is: " + str(J))
print("aantal munten van 1 eurocent is: " + str(L))
