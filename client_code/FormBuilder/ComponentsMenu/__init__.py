from ._anvil_designer import ComponentsMenuTemplate
from anvil import *
from ..ComponentEdit.TextBox import TextBox

class ComponentsMenu(ComponentsMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.new_question = {}

  def short_text_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert")
    short_text_question = alert(content=TextBox(item=self.new_question), large=True, buttons=[("Save", True), ("Cancel", False)])
    if short_text_question:
      print(self.new_question)
    
    

