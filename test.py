import mock
import builtins
import main


def test_q1(capfd):
    input_output = {
        '2':'Par\n',
        '3': 'Impar\n',
        '20':'Par\n',
        '33':'Impar\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v

def test_q2(capfd):
    input_output = {
        'abcdef':'def\n',
        'texto': 'to\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q2()
            out, err = capfd.readouterr()
            assert out == v
