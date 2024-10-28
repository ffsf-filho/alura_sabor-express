from livro import Livro



def main():
    livro1 = Livro("Aprendendo Python", "John Doe", 2022)
    livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
    livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

    print(livro1)
    print(livro2)
    print()
    print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
    livro3.emprestar()
    print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

    
if __name__ == '__main__':
    main()