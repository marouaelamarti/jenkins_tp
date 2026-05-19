
import sys

print("=" * 40)
print("Bienvenue dans mon premier job Jenkins !")
print("=" * 40)

if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = "Étudiant Jenkins"

print(f"Bonjour {nom}, ton job Jenkins a réussi !")

a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

assert a + b == 15, "Le test a échoué !"
print("✅ Tous les tests passent avec succèsprint("=" * 40)
print("bienvenue dans mon premier job jenkins!"
print("=" * 40)
nom=input("quel est ton nom?")
print(f"bonjour {nom},ton job jenkins a reussi!")
a=10
b=5
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
