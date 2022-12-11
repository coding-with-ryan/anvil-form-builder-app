from ._anvil_designer import FormBuilderTemplate
from anvil import *
from .AddComponentForm import AddComponentForm

class FormBuilder(FormBuilderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(AddComponentForm(Label(text="This is the label")))

