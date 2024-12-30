# Test case for validating search functionality
import time

from pageobjects import TableSortSearchPage


def test_search_functionality(driver):
    page = TableSortSearchPage(driver)
    page.load()

    # Perform search
    search_query = "New York"
    page.search(search_query)

    # Validate the row count
    displayed_row_count = page.get_table_row_count()
    assert displayed_row_count == 5, f"Expected 5 rows, but got {displayed_row_count}"

    # Validate total entries text
    total_entries_text = page.get_total_entries_text()
    expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
    assert total_entries_text == expected_text, f"Expected '{expected_text}', but got: {total_entries_text}"