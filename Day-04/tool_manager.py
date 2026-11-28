import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Tools.current_time import get_current_time
from Tools.roll_dice import roll_dice
from Tools.generate_password import generate_password

def execute_tool(user_input):
    if "time" in user_input.lower():
       return get_current_time()
      
    if "dice" in user_input.lower():
        return roll_dice()
        
    if "password" in user_input.lower():
        return generate_password()
      
    return None