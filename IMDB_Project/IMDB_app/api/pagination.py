from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MovieListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    # page_size_query_param = 'size'
    # max_page_size = 10
    # last_page_strings = 'end'

class MovieListLOPagination(LimitOffsetPagination):
    default_limit = 7
    limit_query_param = 'limit'
    offset_query_param = 'start'

class MovieListCPagination(CursorPagination):
    page_size = 5
    cursor_query_param = 'record'