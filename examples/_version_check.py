"""
Python Version Check
====================
Shared utility to check Python version compatibility.
"""

import sys
from typing import Tuple


def check_python_version(min_version: Tuple[int, int] = (3, 7)) -> None:
    """
    Check if Python version meets minimum requirements.
    
    Args:
        min_version: Minimum Python version as (major, minor) tuple
        
    Raises:
        RuntimeError: If Python version is too old
    """
    if sys.version_info < min_version:
        raise RuntimeError(
            f"Python {min_version[0]}.{min_version[1]}+ required. "
            f"Current version: {sys.version_info.major}.{sys.version_info.minor}"
        )
