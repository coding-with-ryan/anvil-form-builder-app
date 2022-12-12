from ._anvil_designer import FormBuilderTemplate
from anvil import *
from .AddComponentForm import AddComponentForm
from .ComponentsMenu import ComponentsMenu

class FormBuilder(FormBuilderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_question_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    question = {}
    new_question = alert(content=ComponentsMenu(item=question), large=True, dismissible=True)

    print(question)
    
    

