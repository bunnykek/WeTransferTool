from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'WeTransferTool',         # How you named your package folder (MyLib)
  packages = ['WeTransferTool'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'WeTransfer unofficial API wrapper written in python facilitating features like uploading and downloading files and folders',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'bunny',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/bunnykek/WeTransferTool',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bunnykek/WeTransferTool',    # I explain this later on
  keywords = ['api', 'wetransfer', 'wrapper', 'upload', 'download'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ]
)