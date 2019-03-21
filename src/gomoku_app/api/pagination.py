"""Pagination file containing classes responsible for handling pagination"""
from rest_framework import pagination


class StandardResultsPagination(pagination.PageNumberPagination):
    """Setting standard pagination for the results"""
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000
