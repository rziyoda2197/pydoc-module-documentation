import pydoc

class Modul:
    def __init__(self):
        pass

    def metod1(self):
        """Metod1"""
        return "Metod1"

    def metod2(self):
        """Metod2"""
        return "Metod2"

def main():
    modul = Modul()
    pydoc.html.help(modul)

if __name__ == "__main__":
    main()
```

Kodni ishga tushirganda, `pydoc.html.help(modul)` funksiyasi modulning hujjatini HTML faylga aylantiradi.
