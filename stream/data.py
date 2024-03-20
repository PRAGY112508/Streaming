import random
import string
from typing import Callable


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))


BufferData = str

Buffer = Callable[[], BufferData]

# Callable[[], BufferData] is a type hint in Python that indicates that the 
# object being defined is a callable (i.e. a function or a class with a __call__ method) 
# that takes no arguments and returns an object of type BufferData.