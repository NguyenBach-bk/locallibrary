from django.shortcuts import render
from django.urls import reverse
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Define constants
PAGINATION_SIZE = 10

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    
    # Available books (status = 'a' for Available)
    num_instances_available = BookInstance.objects.filter(
        status__exact='a'
    ).count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = PAGINATION_SIZE


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        # Get the list of genres as a list to join in the template
        context['genres'] = book.genre.values_list('name', flat=True)

        # Get the list of book instances
        context['book_copies'] = book.bookinstance_set.all()

        # Create a link to the author's detail page (if available)
        try:
            author = book.author
            context['author_url'] = reverse('author-detail', args=[str(author.id)])
        except:
            context['author_url'] = '#'

        return context
