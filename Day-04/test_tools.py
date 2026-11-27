


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Tools.current_time import get_current_time
from Tools.roll_dice import roll_dice
from Tools.generate_password import generate_password

print(get_current_time())
print(roll_dice())
print(generate_password())
