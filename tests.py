from conto import Conto

c1 = Conto("Elara", "IT99L123456789", 500)

assert c1.intestatario == "Elara"
assert c1.iban == "IT99L123456789"
assert c1.saldo == 500

print("Test Passo 1: Superato con successo! ✅")