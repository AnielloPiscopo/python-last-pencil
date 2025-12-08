class ConversionError(ValueError):
    """Raised when a value cannot be converted."""
    pass

class ConstraintError(ValueError):
    """Raised when a value violates logical constraints."""
    pass
