from django.shortcuts import render
from .models import Book, Author, Profile, Tag, Review

def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context)

def Atividade(request):
        
    livros_por_autor = Book.objects.filter(author__name='joão' )
    livros_por_tag = Book.objects.filter(tags__name__icontains =  'Ciência')
    autores_por_biografia = Author.objects.filter(bio__icontains = 'olá')
    livros_avaliacoes_altas = Book.objects.filter(reviews__rating__gte = 4)
    perfil_usuario_website = Profile.objects.exclude(website = None)
    livros_sem_avaliacao = Book.objects.filter(tags__isnull = True)
    autor_mais_livros = Author.objects.all().order_by("books").values()
    livros_resumo_longos = Book.objects.filter(summary__gt = 150)
    avaliacao_livro_autor = Review.objects.filter( book__author__name = "joão")
    livros_muitas_tags = Book.objects.filter(tags__gt = 1)

    context = {
        'livros_por_autor' : livros_por_autor,
        'livros_por_tag': livros_por_tag,
        'autores_por_biografia': autores_por_biografia,
        'livros_avaliacoes_altas': livros_avaliacoes_altas,
        'perfil_usuario_website': perfil_usuario_website,
        'livros_sem_avaliacao': livros_sem_avaliacao,
        'autor_mais_livros': autor_mais_livros,
        'livros_resumo_longos': livros_resumo_longos,
        'avaliacao_livro_autor': avaliacao_livro_autor,
        'livros_muitas_tags': livros_muitas_tags,
    }

    return render(request, 'core/teste1.html', context=context)






