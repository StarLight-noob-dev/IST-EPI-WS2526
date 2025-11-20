def chessboard(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        raise ValueError("n und m müssen ganze Zahlen sein")
    if n < 0 or m < 0:
        raise ValueError("Bitte geben Sie positive Zahlen ein")
    for i in range(1,m+1):
        if i % 2 != 0:
            block = "0  1  "
        else:
            block = "1  0  "
        if n % 2 != 0:
            ender = "0"
        else:
            ender = ""
        print(block * int(n/2) + ender)


#CTKonstante bedeutet Catalansche Konstante
def CTkonstante (n):
    Gesamtezahl = 0
    for i in range(n+1):
        if i%2 == 0:
            Wert = 1/((2*i+1)**2)
        else:
            Wert = (-1)/((2*i+1)**2)
        Gesamtezahl += Wert
    return Gesamtezahl


if __name__ == "__main__":
    #chessboard(5,5)
    print(CTkonstante(9))
    print(CTkonstante(10))
    print(CTkonstante(11))