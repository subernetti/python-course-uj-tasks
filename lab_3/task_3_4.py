# Zadanie 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) 
# i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu 
# z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać 
# komunikat o błędzie i kontynuować pracę.

while 1:
    x = input("Podaj liczbe rzeczywista x: ")

    if(x == "stop"):
        break

    try:
        x = float(x)
        print(f"Liczba: {x}, trzecia potęga: {x ** 3}")
    except ValueError:
        print('Błąd! Dopuszczalny input to x (float) lub "stop"')
    

