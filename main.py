
metai_nuo = int(input("Įveskite metus nuo: "))
metai_iki = int(input("Įveskite metus iki: "))

print(f"Keliamieji metai nuo {metai_nuo} iki {metai_iki}:")
for metai in range(metai_nuo, metai_iki + 1):

    if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
        print(metai)
input("Noredami uzdaryti paspauskite ENTER")

