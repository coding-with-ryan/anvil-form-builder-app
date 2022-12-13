from ._anvil_designer import ComponentsMenuTemplate
from anvil import *
from ..ComponentEdit.TextBox import TextBox

from .. import Globals

class ComponentsMenu(ComponentsMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.question = {}

  def short_text_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert")
    question = alert(content=TextBox(item=self.question), large=True, buttons=[("Save", True), ("Cancel", False)])
    if question:
      print(question)
      get_open_form().raise_event("x-save-question", new_question=question)
      Globals.NUMBER_OF_QUESTIONS += 1

  def long_text_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert")
    question = alert(content=TextBox(item=self.question), large=True, buttons=[("Save", True), ("Cancel", False)])
    if question:
      get_open_form().raise_event("x-save-question", new_question=question)
      Globals.NUMBER_OF_QUESTIONS += 1
    
    

