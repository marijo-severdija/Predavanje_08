from random import randint

attempt = 0
max_attempt = 5
poruka1 = "Broj je veći od zamišljenog..."
poruka2 = "Broj je manji od zamišljenog..."
poruka3 = "Bravo, pogodili ste zamišljen broj!"
poruka4 = "Iskoristili ste max broj pokušaja"

print("Igra pogađanja zamišljenog broja u rasponu 1-30...")
a = randint(1, 30)

while attempt <= max_attempt:
    b = int(input("Probajte pogoditi zamišljeni broj: "))
    attempt += 1
    if b == a:
        print(poruka3)
        print(f"Imali ste {attempt} pokušaja")
        if attempt == max_attempt:
            print(poruka4)
        break
    elif b > a:
        print(poruka2)
        print(f"Imali ste {attempt} pokušaja")
        print(f"Preostalo Vam je {max_attempt - attempt} pokušaja\n")
        if attempt == max_attempt:
            print(poruka4)
            break
    elif b < a:
        print(poruka1)
        print(f"Imali ste {attempt} pokušaja")
        print(f"Preostalo Vam je {max_attempt - attempt} pokušaja\n")
        if attempt == max_attempt:
            print(poruka4)
            break
