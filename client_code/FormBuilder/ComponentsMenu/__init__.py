from ._anvil_designer import ComponentsMenuTemplate
from anvil import *
from ..ComponentEdit.TextBox import TextBox

class ComponentsMenu(ComponentsMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def short_text_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().close_alert()
    # alert(content=TextBox())
    
    

