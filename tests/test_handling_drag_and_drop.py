from pages.droppable_page import DragAndDropPage
from config.settings import Config
from data.data_testing import DRAG_AND_DROP

def test_handling_drag_and_drop(browser):
    page = DragAndDropPage(browser)
    
    #Navigate to the website
    page.open_droppable_page()
    
    #Verify URL and title page 
    assert page.current_url_of_droppable() == Config.DROPPABLE_URL
    assert page.get_page_title_of_droppable() == DRAG_AND_DROP["title_page"]
    
    #Switch to inline frame of website
    page.switch_to_iframe()
    
    #Drag & drop the item then verify the result
    page.drag_and_drop_item()
    assert page.get_actual_result() == DRAG_AND_DROP["expected_result"]