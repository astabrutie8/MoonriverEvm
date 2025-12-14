# test_moonriverevm.py
"""
Tests for MoonriverEvm module.
"""

import unittest
from moonriverevm import MoonriverEvm

class TestMoonriverEvm(unittest.TestCase):
    """Test cases for MoonriverEvm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MoonriverEvm()
        self.assertIsInstance(instance, MoonriverEvm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MoonriverEvm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
