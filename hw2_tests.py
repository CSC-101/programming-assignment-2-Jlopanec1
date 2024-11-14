import data
import hw2
import unittest
from typing import Optional

# Write your test cases for each part below.


    # Part 1
class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

def create_rectangle(p1, p2):
    left_x = min(p1.x, p2.x)
    right_x = max(p1.x, p2.x)

    top_y = max(p1.y, p2.y)
    bottom_y = min(p1.y, p2.y)

    top_left = Point(left_x, top_y)
    bottom_right = Point(right_x, bottom_y)

    return Rectangle(top_left, bottom_right)

p1 = Point(4,3)
p2 = Point(8,8)
rect = create_rectangle(p1, p2)
print(f"Top left is {rect.top_left.x},{rect.top_left.y}")
print(f"Bottom right is {rect.bottom_right.x}, {rect.bottom_right.y}")
p3 = Point(0,0)
p4 = Point(10,10)
rect2 = create_rectangle(p3, p4)
print(f"Top left is {rect2.top_left.x},{rect2.top_left.y}")
print(f"Bottom right is {rect2.bottom_right.x}, {rect2.bottom_right.y}")


    # Part 2
class Duration:
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds
    def convert_seconds(self):
        return self.minutes * 60 + self.seconds
def shorter_duration_than(d1,d2):
    if d1.convert_seconds() < d2.convert_seconds():
        return True
    else:
        return False
duration1 = Duration(1, 40)
duration2 = Duration(2, 30)
print(shorter_duration_than(duration1, duration2))
duration3 = Duration(11, 40)
duration4 = Duration(10, 100)
print(shorter_duration_than(duration3, duration4))

    # Part 3
class Song:
    def __init__(self, artist: str, title: str, duration:Duration):
        self.title = title
        self.duration = duration
class Duration:
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds
    def convert_seconds(self):
        return self.minutes * 60 + self.seconds
def songs_shorter_than(songs, total_duration):
    total_seconds = total_duration.convert_seconds()
    return [song for song in songs if song.duration.convert_seconds() < total_seconds]
song1 = Song("Adam", "Blouse", Duration(2,40))
song2 = Song("Bayle", "Rings",Duration(1, 5))
song3 = Song("Cha", "Ipon",Duration(0, 45))
songs = [song1,song2,song3]
total_duration = Duration (4, 0)
shorter_songs = songs_shorter_than(songs, total_duration)
for song in shorter_songs:
    print(song.title)
song4 = Song("Adam", "Blouse", Duration(2, 40))
song5 = Song("Bayle", "Rings", Duration(1, 5))
song6 = Song("Cha", "Ipon", Duration(0, 45))
songs2 = [song4, song5, song6]
total_duration = Duration(4, 0)
shorter_songs2 = songs_shorter_than(songs, total_duration)
for song in shorter_songs2:
    print(song.title)

    # Part 4
    class Song:
        def __init__(self, artist: str, title: str, minutes: int, seconds: int):
            self.artist = artist
            self.title = title
            self.minutes = minutes
            self.seconds = seconds

        def duration_in_seconds(self):
            return self.minutes * 60 + self.seconds


    class Duration:
        def __init__(self, minutes, seconds):
            # Ensure the seconds are within 0-59
            if seconds >= 60:
                additional_minutes = seconds // 60
                seconds = seconds % 60
                minutes += additional_minutes
            elif seconds < 0:
                raise ValueError("Seconds must not be negative")

            self.minutes = minutes
            self.seconds = seconds

        def __str__(self):
            return f"{self.minutes:02}:{self.seconds:02}"


    def running_time(songs, playlist):
        total_seconds = 0
        for index in playlist:
            if 0 <= index < len(songs):  # Check if the index is valid
                total_seconds += songs[index].duration_in_seconds()
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Duration(minutes, seconds)


    songs = [
        Song("Song1", "Title1", 3, 20),
        Song("Song2", "Title2", 4, 5),
        Song("Song3", "Title3", 2, 30),
        Song("Song4", "Title4", 2, 1)
    ]
    playlist = [1,2,3]
    result = running_time(songs, playlist)
    print(result)
    playlist2 = [4,4,4]
    result2 = running_time(songs, playlist2)
    print(result2)
    # Part 5
    def validate_route(city_links, route):
        links_set = {frozenset(link) for link in city_links}
        for i in range(len(route) - 1):
            pair = frozenset([route[i], route[i + 1]])
            if pair not in links_set:
                return False
        return True


    city_links = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
    route1 = ['san luis obispo', 'atascadero']
    print(validate_route(city_links, route1))
    route2 = []
    print(validate_route(city_links, route2))
    # Part 6
def longest_repetition(list: list[int]) -> Optional[int]:
    if not list:
        return None
    max_len = 0
    max_start = 0
    current_len = 1
    current_start = 0
    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_len = 1
            current_start = i
    if current_len > max_len:
        max_len = current_len
        max_start = current_start
    return max_start
list = [2,2,2,3,3,4,4,1,1,1,1]
print(longest_repetition(list))
list2 = []
print(longest_repetition(list2))




if __name__ == '__main__':
    unittest.main()
