import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_books(self):      #1
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert collector.books_genre['Властелин колец'] == ''

    def test_add_new_book_length_more_40(self):     #2
        collector = BooksCollector()
        collector.add_new_book('о' * 41)
        assert "оооооооооооооооооооооооооооооооооооооооооооооо" not in collector.books_genre

    def test_add_new_book_length_is_0(self):    #3
        collector = BooksCollector()
        collector.add_new_book('')
        assert "" not in collector.books_genre

    @pytest.mark.parametrize('books, genre', [('Властелин колец', 'Фэнтэзи'),        #4
                                              ('Чужой', 'Ужасы')])
    def test_get_list_of_favorites_books_have_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()


    def test_set_book_genre(self):     #5
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_book_genre('Чужой') == 'Ужасы'

    def test_set_book_genre_invalid(self):  #6
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Роман')
        assert collector.get_book_genre('Чужой') == ''

    def test_get_books_with_specific_genre(self):   #7
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Чужой']

    def test_get_books_for_children_list_is_not_empty(self):    #8
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Фантастика')
        assert 'Чужой' in collector.get_books_for_children()

    def test_get_books_for_children_list_is_empty(self):    #9
        collector = BooksCollector()
        collector.add_new_book('Астрал')
        collector.set_book_genre('Астрал', 'Ужасы')
        assert 'Астрал' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):   #10
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):  #11
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_set_and_get_genre(self):       #12
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        assert collector.get_book_genre('Чужой') == 'Ужасы'

    def test_adding_book_genre(self):       #13
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        assert collector.get_book_genre('Чужой') == ''

    def test_books_with_no_genre(self):     #14
        collector = BooksCollector()
        collector.add_new_book('Бильбо')
        assert collector.get_books_with_specific_genre('') == []

    def test_invalid_genre(self):       #15
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        books_with_invalid_genre = collector.get_books_with_specific_genre('Пьеса')
        assert books_with_invalid_genre == []

    def test_get_books_genre(self):     #16
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        assert collector.get_books_genre() == {'Чужой': ''}

    def test_get_books_for_children_no_books(self):     #17
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    def test_add_new_book_add_two_books(self):  #18
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.add_book_in_favorites('Чужой')
        collector.add_book_in_favorites('Чужой')
        assert collector.get_list_of_favorites_books().count('Чужой') == 1