import data
import unittest


class TestCases(unittest.TestCase):
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(point.x, 7)
        self.assertAlmostEqual(point.y, 20)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(point.x, 4)
        self.assertAlmostEqual(point.y, 19)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual(repr(point), 'Point(5, 75)')


    def test_Duration_1(self):
        duration = data.Duration(1, 20)
        self.assertEqual(duration.minutes, 1)
        self.assertEqual(duration.seconds, 20)


    def test_Duration_2(self):
        duration = data.Duration(4, 19)
        self.assertEqual(duration.minutes, 4)
        self.assertEqual(duration.seconds, 19)


    def test_Duration_eq_1(self):
        duration1 = data.Duration(1, 20)
        duration2 = data.Duration(1, 20)
        self.assertEqual(duration1, duration2)


    def test_Duration_eq_2(self):
        duration1 = data.Duration(1, 20)
        self.assertEqual(duration1, duration1)


    def test_Duration_eq_3(self):
        duration1 = data.Duration(1, 20)
        duration2 = data.Duration(2, 20)
        self.assertNotEqual(duration1, duration2)


    def test_Duration_eq_4(self):
        duration = data.Duration(1, 20)
        other = 1.20
        self.assertNotEqual(duration, other)


    def test_Duration_repr(self):
        duration = data.Duration(5, 14)
        self.assertEqual(repr(duration), 'Duration(5, 14)')


    def test_Song_1(self):
        song = data.Song('Artist', 'Title', data.Duration(3, 21))
        self.assertEqual(song.artist, 'Artist')
        self.assertEqual(song.title, 'Title')
        self.assertEqual(song.duration, data.Duration(3, 21))


    def test_Song_eq_1(self):
        song1 = data.Song('Artist', 'Title', data.Duration(3, 21))
        song2 = data.Song('Artist', 'Title', data.Duration(3, 21))
        self.assertEqual(song1, song2)


    def test_Song_eq_2(self):
        song = data.Song('Artist', 'Title', data.Duration(3, 21))
        self.assertEqual(song, song)


    def test_Song_eq_3(self):
        song1 = data.Song('Artist1', 'Title', data.Duration(3, 21))
        song2 = data.Song('Artist2', 'Title', data.Duration(3, 21))
        self.assertNotEqual(song1, song2)


    def test_Song_eq_4(self):
        song1 = data.Song('Artist', 'Title1', data.Duration(3, 21))
        song2 = data.Song('Artist', 'Title2', data.Duration(3, 21))
        self.assertNotEqual(song1, song2)


    def test_Song_eq_5(self):
        song1 = data.Song('Artist', 'Title', data.Duration(2, 21))
        song2 = data.Song('Artist', 'Title', data.Duration(3, 21))
        self.assertNotEqual(song1, song2)


    def test_Song_eq_6(self):
        song = data.Song('Artist', 'Title', data.Duration(2, 21))
        other = 1.20
        self.assertNotEqual(song, other)


    def test_Song_repr(self):
        song = data.Song('Artist', 'Title', data.Duration(2, 21))
        self.assertEqual(repr(song),
            "Song('Artist', 'Title', Duration(2, 21))")


    def test_Rectangle_1(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle.top_left, data.Point(7, 20))
        self.assertEqual(rectangle.bottom_right, data.Point(12, 10))


    def test_Rectangle_eq_1(self):
        rectangle1 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        rectangle2 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle1, rectangle2)


    def test_Rectangle_eq_2(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(rectangle, rectangle)


    def test_Rectangle_eq_3(self):
        rectangle1 = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        rectangle2 = data.Rectangle(data.Point(4, 17), data.Point(12, 10))
        self.assertNotEqual(rectangle1, rectangle2)


    def test_Rectangle_eq_4(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        other = 1.20
        self.assertNotEqual(rectangle, other)


    def test_Rectangle_repr(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertEqual(repr(rectangle),
            'Rectangle(Point(7, 20), Point(12, 10))')


if __name__ == '__main__':
    unittest.main()


    class TestCases(unittest.TestCase):
