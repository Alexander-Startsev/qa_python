import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert collector.books_genre['Властелин колец'] == ''

    def test_add_new_book_length_more_40(self):
        collector = BooksCollector()
        collector.add_new_book('о' * 41)
        assert "оооооооооооооооооооооооооооооооооооооооооооооо" not in collector.books_genre

    def test_add_new_book_length_is_0(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert "" not in collector.books_genre

    @pytest.mark.parametrize('books, genre', [('Шерлок Холмс', 'Детективы'),
                                              ('Гарри Поттер', 'Фатнастика')])
    def test_get_list_of_favorites_books_have_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Роман')
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    def test_get_books_for_children_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Мультфильмы')
        assert 'Гарри Поттер' in collector.get_books_for_children()

    def test_get_books_for_children_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        assert 'Пила' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    def test_add_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books().count('Гарри Поттер') == 1

    def test_set_and_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_adding_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_books_with_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        assert collector.get_books_with_specific_genre('') == []

    def test_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        books_with_invalid_genre = collector.get_books_with_specific_genre('Авангардизм')
        assert books_with_invalid_genre == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    def test_get_books_for_children_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []