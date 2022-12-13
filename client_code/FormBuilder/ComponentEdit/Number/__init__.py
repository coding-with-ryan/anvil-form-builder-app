from ._anvil_designer import NumberTemplate
from anvil import *

class Number(NumberTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    from ... import Globals

    self.question_number_label.text = Globals.NUMBER_OF_QUESTIONS + 1
