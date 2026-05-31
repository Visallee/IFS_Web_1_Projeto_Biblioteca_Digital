from django.db import migrations

def criar_categorias(apps, schema_editor):
    Categoria = apps.get_model('biblioteca', 'Categoria')

    categorias = [
        ('Ficção', 'Romances, contos e obras fictícias'),
        ('Fantasia', 'Magia, mundos imaginários e aventura fantástica'),
        ('Ficção Científica', 'Tecnologia, espaço e futuro'),
        ('Terror', 'Histórias de suspense e horror'),
        ('Mistério', 'Investigação e suspense'),
        ('Romance', 'Relacionamentos e histórias amorosas'),
        ('Aventura', 'Exploração e ação'),
        ('Drama', 'Narrativas emocionais e conflitos humanos'),
        ('Biografia', 'Histórias reais de pessoas'),
        ('História', 'Eventos e períodos históricos'),
        ('Geografia', 'Espaço geográfico e sociedade'),
        ('Filosofia', 'Pensamento e reflexão filosófica'),
        ('Psicologia', 'Comportamento e mente humana'),
        ('Religião', 'Espiritualidade e tradições religiosas'),
        ('Ciência', 'Conhecimento científico geral'),
        ('Matemática', 'Álgebra, geometria e cálculo'),
        ('Física', 'Fenômenos físicos e natureza'),
        ('Química', 'Substâncias e reações químicas'),
        ('Biologia', 'Vida e organismos vivos'),
        ('Medicina', 'Saúde e práticas médicas'),
        ('Tecnologia', 'Computação e inovação tecnológica'),
        ('Programação', 'Desenvolvimento de software e código'),
        ('Banco de Dados', 'Modelagem e gerenciamento de dados'),
        ('Redes de Computadores', 'Infraestrutura e comunicação de redes'),
        ('Segurança da Informação', 'Proteção de sistemas e dados'),
        ('Engenharia', 'Projetos e soluções técnicas'),
        ('Direito', 'Leis e sistema jurídico'),
        ('Administração', 'Gestão e negócios'),
        ('Economia', 'Mercados e finanças'),
        ('Educação', 'Ensino e aprendizagem'),
        ('Didático', 'Livros escolares e acadêmicos'),
        ('Arte', 'Pintura, escultura e expressão artística'),
        ('Música', 'Teoria e prática musical'),
        ('Cinema', 'Filmes e audiovisual'),
        ('HQ e Mangá', 'Quadrinhos e mangás'),
        ('Infantil', 'Literatura para crianças'),
        ('Juvenil', 'Literatura para jovens'),
        ('Autoajuda', 'Desenvolvimento pessoal'),
        ('Culinária', 'Receitas e gastronomia'),
        ('Esportes', 'Atividade física e esportes'),
        ('Turismo', 'Viagens e destinos'),
        ('Idiomas', 'Aprendizado de línguas'),
        ('Poesia', 'Poemas e literatura poética'),
    ]

    for nome, descricao in categorias:
        Categoria.objects.get_or_create(
            nome=nome,
            defaults={'descricao': descricao}
        )

def remover_categorias(apps, schema_editor):
    Categoria = apps.get_model('biblioteca', 'Categoria')
    Categoria.objects.filter(
        nome__in=['Ficção', 'Tecnologia', 'História', 'Ciência']
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_categoria_options_alter_livro_options_and_more'),
    ]

    operations = [
        migrations.RunPython(
            criar_categorias,
            remover_categorias
        ),
    ]