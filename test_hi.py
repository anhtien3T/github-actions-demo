from hi import say_hi

def test_say_hi():
    assert say_hi("World") == "Hi, World!"
    assert say_hi("Grok") == "Hi, Grok!"