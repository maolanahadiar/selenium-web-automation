from pages.droppable_page import DragAndDropPage
from config.settings import Config
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_handling_drag_and_drop(browser):
    page = DragAndDropPage(browser)
    
    #Navigate to the website
    page.open_droppable_page()
    
    #Verify URL and title page 
    assert page.current_url_of_droppable() == Config.DROPPABLE_URL
    assert page.get_page_title_of_droppable() == TITLES["drag_and_drop"]["page_title"]
    
    #Switch to inline frame of website
    page.switch_to_iframe()
    
    #Drag & drop the item then verify the result
    page.drag_and_drop_item()
    assert page.get_actual_result() == MESSAGES["drag_and_drop"]["expected_result"]