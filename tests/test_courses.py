import pytest
from playwright.sync_api import expect

@pytest.mark.regression
@pytest.mark.courses

def test_empty_courses_list1(chromium_page_with_state):
    course = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course).to_contain_text('Courses')

    icons = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icons).to_be_visible()

    text_1 = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_1).to_be_visible()
    expect(text_1).to_contain_text('There is no results')

    text_2 = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_2).to_contain_text("Results from the load tests pipeline will be displayed here")

