import unittest
from unittest.mock import patch, mock_open
from read_file_logic import read_file


# Test file reading logic
class TestReadFileLogic(unittest.TestCase):
    
    # Test if read_file correctly reads file content
    def test_read_file_success(self):
        mock_content = "author: John\n title: Test\n date: 2025-04-30\n"
        with patch("builtins.open", mock_open(read_data=mock_content)):
            content = read_file("dummy.txt")
            self.assertEqual(content, mock_content)
    # Test if FileNotFoundError is raised for misssing file
    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")

class TestMetadataExtraction(unittest.TestCase):
    def setUp(self):
        from main_GUI import DocumentScannerGUI
        self.gui = DocumentScannerGUI
        self.instance = self.gui.__new__(self.gui) 
        
    # Test metadata extraction
    def test_extract_metadata(self):
        sample = """date: 2025-04-30
author: Cassie Dillion
title: Artificial Intelligence
AI in healthcare is growing fast."""
        result = self.instance.extract_metadata(sample)
        expected = {
            'date': '2025-04-30',
            'author': 'Cassie Dillion',
            'title': 'Artificial Intelligence'
        }
        self.assertEqual(result, expected)

    def test_extract_metadata_missing_fields(self):
        sample = "No metadata here"
        result = self.instance.extract_metadata(sample)
        self.assertEqual(result, {'author': 'Unknown', 'title': 'Unknown', 'date': 'Unknown'})

if __name__ == "__main__":
    unittest.main()
