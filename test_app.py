import unittest
import os
from app import app, allowed_image_file, allowed_video_file

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Create uploads directory if it doesn't exist
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
    
    def test_home_page(self):
        """Test that home page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'EXIF Data Extractor', response.data)
    
    def test_allowed_image_file(self):
        """Test the allowed image file function"""
        self.assertTrue(allowed_image_file('test.jpg'))
        self.assertTrue(allowed_image_file('test.jpeg'))
        self.assertTrue(allowed_image_file('test.png'))
        self.assertFalse(allowed_image_file('test.gif'))
        self.assertFalse(allowed_image_file('test.txt'))
    
    def test_allowed_video_file(self):
        """Test the allowed video file function"""
        self.assertTrue(allowed_video_file('test.mp4'))
        self.assertTrue(allowed_video_file('test.avi'))
        self.assertTrue(allowed_video_file('test.mov'))
        self.assertTrue(allowed_video_file('test.mkv'))
        self.assertFalse(allowed_video_file('test.gif'))
        self.assertFalse(allowed_video_file('test.txt'))

    def test_no_file_upload(self):
        """Test response when no file is uploaded"""
        response = self.app.post(
            '/',
            data={},
            content_type='multipart/form-data'
        )
        
        # Should return 200 OK but with the default template
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'error', response.data.lower())


if __name__ == '__main__':
    unittest.main()