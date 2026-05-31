from django.db import migrations


def criar_livros(apps, schema_editor):
    Categoria = apps.get_model('biblioteca', 'Categoria')
    Livro = apps.get_model('biblioteca', 'Livro')
    User = apps.get_model('auth', 'User')

    admin = User.objects.first()

    livros = [
        {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': 1899, 'categoria': 'Ficção'},
        {'titulo': 'Memórias Póstumas de Brás Cubas', 'autor': 'Machado de Assis', 'ano': 1881, 'categoria': 'Ficção'},
        {'titulo': 'O Cortiço', 'autor': 'Aluísio Azevedo', 'ano': 1890, 'categoria': 'Ficção'},
        {'titulo': 'O Senhor dos Anéis', 'autor': 'J. R. R. Tolkien', 'ano': 1954, 'categoria': 'Fantasia'},
        {'titulo': 'O Hobbit', 'autor': 'J. R. R. Tolkien', 'ano': 1937, 'categoria': 'Fantasia'},
        {'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J. K. Rowling', 'ano': 1997, 'categoria': 'Fantasia'},
        {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949, 'categoria': 'Ficção Científica'},
        {'titulo': 'Admirável Mundo Novo', 'autor': 'Aldous Huxley', 'ano': 1932, 'categoria': 'Ficção Científica'},
        {'titulo': 'Duna', 'autor': 'Frank Herbert', 'ano': 1965, 'categoria': 'Ficção Científica'},
        {'titulo': 'Drácula', 'autor': 'Bram Stoker', 'ano': 1897, 'categoria': 'Terror'},
        {'titulo': 'It: A Coisa', 'autor': 'Stephen King', 'ano': 1986, 'categoria': 'Terror'},
        {'titulo': 'O Iluminado', 'autor': 'Stephen King', 'ano': 1977, 'categoria': 'Terror'},
        {'titulo': 'Sherlock Holmes: Um Estudo em Vermelho', 'autor': 'Arthur Conan Doyle', 'ano': 1887,
         'categoria': 'Mistério'},
        {'titulo': 'Sapiens', 'autor': 'Yuval Noah Harari', 'ano': 2011, 'categoria': 'História'},
        {'titulo': 'A República', 'autor': 'Platão', 'ano': -380, 'categoria': 'Filosofia'},
        {'titulo': 'O Príncipe', 'autor': 'Nicolau Maquiavel', 'ano': 1532, 'categoria': 'Filosofia'},
        {'titulo': 'Uma Breve História do Tempo', 'autor': 'Stephen Hawking', 'ano': 1988, 'categoria': 'Ciência'},
        {'titulo': 'O Gene', 'autor': 'Siddhartha Mukherjee', 'ano': 2016, 'categoria': 'Biologia'},
        {'titulo': 'Cosmos', 'autor': 'Carl Sagan', 'ano': 1980, 'categoria': 'Ciência'},
        {'titulo': 'Clean Code', 'autor': 'Robert C. Martin', 'ano': 2008, 'categoria': 'Programação'},
        {'titulo': 'The Pragmatic Programmer', 'autor': 'Andrew Hunt', 'ano': 1999, 'categoria': 'Programação'},
        {'titulo': 'Código Limpo', 'autor': 'Robert C. Martin', 'ano': 2008, 'categoria': 'Programação'},
        {'titulo': 'Python Crash Course', 'autor': 'Eric Matthes', 'ano': 2015, 'categoria': 'Programação'},
        {'titulo': 'Automate the Boring Stuff with Python', 'autor': 'Al Sweigart', 'ano': 2015,
         'categoria': 'Programação'},
        {'titulo': 'Introdução a Algoritmos', 'autor': 'Thomas H. Cormen', 'ano': 1990, 'categoria': 'Tecnologia'},
        {'titulo': 'Estruturas de Dados e Algoritmos', 'autor': 'Narasimha Karumanchi', 'ano': 2011,
         'categoria': 'Tecnologia'},
        {'titulo': 'Pai Rico, Pai Pobre', 'autor': 'Robert Kiyosaki', 'ano': 1997, 'categoria': 'Economia'},
        {'titulo': 'A Arte da Guerra', 'autor': 'Sun Tzu', 'ano': -500, 'categoria': 'Administração'},
        {'titulo': 'O Homem Mais Rico da Babilônia', 'autor': 'George S. Clason', 'ano': 1926, 'categoria': 'Economia'},
        {'titulo': 'Hábitos Atômicos', 'autor': 'James Clear', 'ano': 2018, 'categoria': 'Autoajuda'},
        {'titulo': 'O Poder do Hábito', 'autor': 'Charles Duhigg', 'ano': 2012, 'categoria': 'Autoajuda'},
        {'titulo': 'Como Fazer Amigos e Influenciar Pessoas', 'autor': 'Dale Carnegie', 'ano': 1936,
         'categoria': 'Autoajuda'},
        {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'ano': 1943, 'categoria': 'Infantil'},
        {'titulo': 'Percy Jackson e o Ladrão de Raios', 'autor': 'Rick Riordan', 'ano': 2005, 'categoria': 'Juvenil'},
    ]

    for item in livros:
        categoria = Categoria.objects.get(nome=item['categoria'])

        Livro.objects.get_or_create(
            titulo=item['titulo'],
            autor=item['autor'],
            defaults={
                'ano_publicacao': item['ano'],
                'categoria': categoria,
                'status': 'disponivel',
                'cadastrado_por': admin,
            }
        )





class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_carregar_categorias'),
    ]

    operations = [
        migrations.RunPython(criar_livros),
    ]