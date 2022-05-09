#!/usr/bin/env python

import sys
from pathlib import Path

env_path = Path(sys.argv[1])

# adds absolute path of package to pip requirements
with open(env_path, 'r') as f:
  env_str = f.read()
env_str = env_str.replace(r'{CWD}', str(env_path.parent))
with open(env_path.parent/'env_local.yml', 'w') as f:
  f.write(env_str)
