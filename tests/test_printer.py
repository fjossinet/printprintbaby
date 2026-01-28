from printprintbaby import print_baby

def test_print_baby(capsys):
    print_baby("test")
    captured = capsys.readouterr()
    assert captured.out.strip() == "test"
