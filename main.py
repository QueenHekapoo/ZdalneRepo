import os

# Funkcja wyświetlająca tekst zachęty
def tekstzachety():
    current_directory = os.getcwd()
    print(f"{current_directory}> ", end="")

# Główna pętla programu
while True:
    tekstzachety()
    command = input().split()

    if not command:
        continue

    if command[0] == "help":
        print("help                 > Wyświetla sposób użycia programu oraz infomracje o komendach")
        print("quit, exit           > Kończy program")
        print("ls                   > Wyświetla pliki")
        print("cr <nazwa>           > Tworzy plik o podanej nazwie")
        print("cd <katalog>         > Przejście do katalogu")
        print("mkdir <katalog>      > Tworzy katalog o podanej nazwie")
        print("o <nazwaPliku>       > Wyświetl zawartość pliku tekstowego")
        print("stat <nazwaPliku>    > Podsumuj zawartość pliku: ilość znaków")
        print("rename <n1> <n2>     > Zmienia nazwę pliku <n1> na <n2>")
        print("find <p> <plik>      > Wyświetla linijki z pliku <plik>, w którym znaleziono tekst <p>")
        print("what                 > ???")
    elif command[0] in ["quit", "exit"]:
        break
    elif command[0] == "ls":
        files = os.listdir()
        for file in files:
            print(file)
    elif command[0] == "cr":
        if len(command) != 2:
            print("Użycie: cr <nazwa>")
        else:
            filename = command[1]
            with open(filename, "w") as file:
                pass
    elif command[0] == "cd":
        if len(command) != 2:
            print("Użycie: cd <katalog>")
        else:
            directory = command[1]
            try:
                os.chdir(directory)
            except FileNotFoundError:
                print("Katalog nie istnieje")
    elif command[0] == "mkdir":
        if len(command) != 2:
            print("Użycie: mkdir <katalog>")
        else:
            directory = command[1]
            os.makedirs(directory, exist_ok=True)
    elif command[0] == "o":
        if len(command) != 2:
            print("Użycie: o <nazwaPliku>")
        else:
            filename = command[1]
            try:
                with open(filename, "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("Plik o podanej nazwie nie istnieje")
    elif command[0] == "stat":
        if len(command) != 2:
            print("Użycie: stat <nazwaPliku>")
        else:
            filename = command[1]
            try:
                with open(filename, "r") as file:
                    content = file.read()
                    print(f"Ilość znaków w pliku: {len(content)}")
            except FileNotFoundError:
                print("Plik nie istnieje")
    elif command[0] == "rename":
        if len(command) != 3:
            print("Użycie: rename <n1> <n2>")
        else:
            old_name = command[1]
            new_name = command[2]
            try:
                os.rename(old_name, new_name)
            except FileNotFoundError:
                print("Plik nie istnieje")
    elif command[0] == "what":
        print("01111010 01101110 01100001 01101100 01100001 01111010 11000101 10000010 01100101 11000101 10011011 00100000 01101101 01101111 01101010 11000100 10000101 00100000 01110011 01100101 01101011 01110010 01100101 01110100 01101110 11000100 10000101 00100000 01110111 01101001 01100001 01100100 01101111 01101101 01101111 11000101 10011011 11000100 10000111 00100001w")
    elif command[0] == "find":
        if len(command) != 3:
            print("Użycie: find <p> <plik>")
        else:
            pattern = command[1]
            filename = command[2]
            try:
                with open(filename, "r") as file:
                    for line in file:
                        if pattern in line:
                            print(line.strip())
            except FileNotFoundError:
                print("Plik nie istnieje")
    else:
        print("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.")
