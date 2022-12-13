from ._anvil_designer import FormBuilderTemplate
from anvil import *
from .AddComponentForm import AddComponentForm
from .ComponentsMenu import ComponentsMenu

from .ComponentDisplay.TextBoxComponent import TextBoxComponent

class FormBuilder(FormBuilderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.set_event_handler('x-save-question', self.save_question)

  def add_question_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_question = alert(content=ComponentsMenu(), large=True, dismissible=True)

  def save_question(self, new_question, **event_args):
    print("New question from form builder: ", new_question)
    new_component = TextBoxComponent(**new_question)
    self.survey_panel.add_component(new_component)
    
    

