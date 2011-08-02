import os, time
import unittest
import numpy as np
import scikits.image.backend
import scikits.image.backend as backend_module
from scikits.image.backend import BackendTester, use_backend, backing
from scikits.image.backend import test1, test2, test3
from numpy.testing import *

class TestBackendTester(BackendTester):
    def __init__(self):
        scikits.image.backends = ["default", "test1", "test2"]
        self.backends_tested = []
        
    def test_test1(self):
        result = test1()
        backend = result.split()[0]
        assert result.endswith("test1") 
        print self.backends_tested, backend
        if backend != "default":
            assert backend not in self.backends_tested
        self.backends_tested.append(backend)
        
        
def test_keyword():
    assert test1() == "default test1"
    assert test1(backend="backend2") == "backend2 test1"
    assert test1(backend="backend1") == "backend1 test1"
    assert test1() == "default test1"
    assert backend_module.test1() == "default test1"
        
        
def test_use_backend():    
    use_backend("backend1")
    assert test1() == "backend1 test1"
    use_backend("backend2")
    assert test1() == "backend2 test1"
    use_backend("default")
    assert test1() == "default test1"
    use_backend()
    assert test1() == "default test1"
    use_backend(None)
    assert test1() == "default test1"
        

def test_use_backend_fallback():
    use_backend(["backend1", "backend2"])
    assert test1() == "backend1 test1"
    assert test2() == "backend2 test2"
    assert test3() == "default test3"


def test_use_backend_fallback_nonexistent():
    use_backend(["wors", "backend2"])
    assert test1() == "backend2 test1"
    use_backend("wors")
    assert test1() == "default test1"
    assert test2(backend="backend1") == "default test2"


def test_documentation_update():
    assert "backend1" in test1.__doc__ and "backend2" in test1.__doc__


def test_backing():
    backends = backing(test1)
    print backends
    for b in ["backend1", "backend2", "default"]:
        assert b in backends


if __name__ == "__main__":
    run_module_suite()
