from expynent.shortcuts import is_private


def test_is_private():
    private_attr = '_IP_CUSTOM'
    public_attr = 'IPv6'
    assert is_private(private_attr)
    assert not is_private(public_attr)
