from apps.core.pagination import StandardResultsSetPagination


def test_default_page_size_is_25():
    assert StandardResultsSetPagination.page_size == 25


def test_max_page_size_is_100():
    assert StandardResultsSetPagination.max_page_size == 100
