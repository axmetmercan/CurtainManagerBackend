from rest_framework import pagination



class DefaultPagination(pagination.LimitOffsetPagination):
    default_limit = 100
    max_limit = 1000

class NumberPagination(pagination.PageNumberPagination):
    page_size = 25
    page_query_param = "pg"
    page_query_param = "pg_size"
