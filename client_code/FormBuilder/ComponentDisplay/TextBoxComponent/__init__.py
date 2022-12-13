from ._anvil_designer import TextBoxComponentTemplate
from anvil import *

class TextBoxComponent(TextBoxComponentTemplate):
  def __init__(self, question, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.item['question_text']=question['question_text'], 
    self.item['question_description']=question['question_description'],
    self.item['question_text']=question['question_number']
