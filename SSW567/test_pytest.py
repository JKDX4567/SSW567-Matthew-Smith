from SSW567.SSW567HW00B import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4
    assert inc_dec.increment(5) == 6

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert inc_dec.decrement(3) == 4
