from ._anvil_designer import TextAreaTemplate
from anvil import *

from ... import Globals

class TextArea(TextAreaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.question_number_label.text = Globals.NUMBER_OF_QUESTIONS + 1
