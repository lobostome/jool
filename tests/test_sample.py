import os
import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

# import os
# def test_create_file(tmpdir):
#     p = tmpdir.mkdir("sub").join("hello.txt")
#     p.write("content")
#     assert p.read() == "content"
#     assert len(tmpdir.listdir()) == 1
#     assert 0

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
