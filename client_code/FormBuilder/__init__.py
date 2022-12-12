from ._anvil_designer import FormBuilderTemplate
from anvil import *
from .AddComponentForm import AddComponentForm
from .ComponentsMenu import ComponentsMenu

class FormBuilder(FormBuilderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.alert_component = None

  def add_question_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.alert_component = alert(content=ComponentsMenu(), large=True, dismissible=True)

  def close_alert(self):
    print("Closing Form")
    print(self.alert_component)
    if self.alert_component is not None:
      self.alert_component.raise_event('x-close-alert')
    

