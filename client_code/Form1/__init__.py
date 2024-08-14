from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    #TODO Update this URL with the Final Draft of the notebook
    self.link_1.url = "https://colab.research.google.com/drive/1t-kpKhJdKRCzBbE_EIG_n9aHuvdX5v3Z?usp=sharing"
    self.link_1.target = "_blank"
  
  def file_loader_1_change(self, file, **event_args):
    # Display the uploaded image in the Image component
    self.uploaded_image.source = file
  def classify_button_click(self, **event_args):
    if self.file_loader_1.file is None:
      self.result_label.text = "Please upload an image first."
      return
    try:
      result = anvil.server.call('classify_image', self.file_loader_1.file)
      self.result_label.text = f"This bird is classified as: {result}"
    except Exception as e:
      self.result_label.text = f"Error: {str(e)}"

# def classify(image):
#     response = anvil.http.request(
#         url="https://colab.research.google.com/drive/1CJADWy5EGjXv58CXN8yEWTxCBVRIa6DB#scrollTo=Me_KGv37H7zl&line=1&uniqifier=1",
#         method="POST",
#         files={'file': image},
#         json=True
#     )
    
    # Extract the classification result from the response
    result = response.get('result', 'No result returned')
    return result