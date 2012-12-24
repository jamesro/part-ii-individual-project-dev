"""
Unit tests for YouTube API.
"""

import unittest
import logging

from api import youtube

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestVideoGangnam(unittest.TestCase):
    """
    Unit tests for the Video class.

    Use Gangnam Style as it's the current most popular video and so
    it's unlikely that it'll be removed.
    """

    def test_title(self):
        gangnam_style_url = "http://www.youtube.com/watch?v=9bZkp7q19f0"
        video = youtube.Video.from_web_url(gangnam_style_url)
        self.assertIn("psy - gangnam",video.title().lower())

    def test_description(self):
        gangnam_style_url = "http://www.youtube.com/watch?v=9bZkp7q19f0"
        video = youtube.Video.from_web_url(gangnam_style_url)
        self.assertIn("http://www.facebook.com/officialpsy",video.description().lower())

    def test_duration(self):
        gangnam_style_url = "http://www.youtube.com/watch?v=9bZkp7q19f0"
        video = youtube.Video.from_web_url(gangnam_style_url)
        duration = 4*60 + 13
        self.assertGreater(video.duration(),duration-2)
        self.assertLess(video.duration(),duration+2)

    def test_related(self):
        gangnam_style_url = "http://www.youtube.com/watch?v=9bZkp7q19f0"
        video = youtube.Video.from_web_url(gangnam_style_url)
        related = video.related()
        self.assertGreater(len(related),5)

class TestVideoCollection(unittest.TestCase):
    """
    Unit tests for the VideoCollection class.

    Use popular music tracks as unlikely to be removed.
    """

    _videos = [
        "http://www.youtube.com/watch?v=9bZkp7q19f0", # PSY - GANGNAM STYLE
        "http://www.youtube.com/watch?v=lJqbaGloVxg", # James Arthur - Impossible - Official Single
        "http://www.youtube.com/watch?v=kYtGl1dX5qI", # will.i.am - Scream & Shout ft. Britney Spears
        "http://www.youtube.com/watch?v=bqIxCtEveG8", # Labrinth feat. Emeli Sande - Beneath Your Beautiful
        "http://www.youtube.com/watch?v=KHF9itPLUo4" # Johnny Cash - I Walk the Line
    ]

    def test_init(self):
        videos = youtube.VideoCollection(self._videos)

    def test_len(self):
        videos = youtube.VideoCollection(self._videos)
        self.assertEqual(len(videos),len(self._videos))

if __name__ == "__main__":
    unittest.main()