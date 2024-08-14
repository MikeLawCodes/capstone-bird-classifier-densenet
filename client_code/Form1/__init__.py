from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    self.link_1.url = "https://colab.research.google.com/drive/1CJADWy5EGjXv58CXN8yEWTxCBVRIa6DB?usp=sharing"
    self.link_1.target = "_blank"

  def classify_button_click(self, **event_args):
    if self.file_loader_1.file is None:
      self.result_label.text = "Please upload an image first."
      return
    try:
      result = anvil.server.call('classify_image', self.file_loader_1.file)
      bird_name = result['result']
      self.result_label.text = f"Bird Classification: {bird_name}"
    except Exception as e:
      self.result_label.text = f"Error: {str(e)}"

  def file_loader_1_change(self, **event_args):
    if self.file_loader_1 is None:
      return
    if self.file_loader_1 is not None:
      self.uploaded_image.source = self.file_loader_1.file