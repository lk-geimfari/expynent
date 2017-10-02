def is_private(pattern):
    """
    Check availability of pattern.
    """
    if pattern:
        return pattern.startswith('_')
