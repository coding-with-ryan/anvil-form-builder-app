from ._anvil_designer import AddComponentFormTemplate
from anvil import *

class AddComponentForm(AddComponentFormTemplate):
  def __init__(self, component, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_component(component)

    # Any code you write here will run before the form opens.
