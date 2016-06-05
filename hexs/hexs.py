"""Hex string formating."""

# Append 0 if the length of s is odd.
make_even = lambda s: '0' + s if len(s) % 2 else s

def is_hex(s):
    """Return whether s is a hex string."""
    try:
        int(s, 16)
    except (TypeError, ValueError):
        return False
    return True

def format_hex(s):
    """Remove extraneous characters from s and make its length even."""
    while s.startswith('0x'):
        s = s[2:]
    return make_even(s.rstrip('L'))

def hexs(arg):
    """Return the formatted hex representation of arg."""
    return format_hex(hex(arg))

__all__ = (
    'is_hex',
    'format_hex',
    'hexs',
)
