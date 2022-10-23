from helloworld import hello_world
#writing a test using pytest
def test_hello_world(capsys):#function starting with 'test' is recognised by pytest
    hello_world()
    out, _ = capsys.readouterr()#takes the output and stores it in out
    assert out == "Hello World!\n"#checks whether 'out' matches the expected result
