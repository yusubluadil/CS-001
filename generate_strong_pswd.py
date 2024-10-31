"""
Güclü şifrə generate edən funksiya yazın.
Araşdırılmalı mövzu random moduludu bu hissədə + string modulundan da istifadə edə bilərsiniz. 
"""

import string
import random

symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def generate_strong_pswd(length: int=8) -> str:
    pswd_symbols_list = random.choices(symbols, k=length)
    pswd = ''.join(pswd_symbols_list)
    return pswd


pswd = generate_strong_pswd(24)
print(pswd)
