import os
import sys
if not __package__:
  path = os.path.join(os.path.dirname(__file__), os.pardir)
  sys.path.insert(0, path)

import neural_gen
neural_gen.main()
