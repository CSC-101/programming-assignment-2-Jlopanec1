import data
from data import Point
from typing import Optional
# Write your functions for each part in the space below.
# Part 1
#Purpose: Create a rectangle
#Input: Points
#Output: Points
#Ex: [3,3], [4,4]
#Result: [3,4], [4,3]
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
p1 = Point(2,2)
p2 = Point(4,4)
rect = create_rectangle(p1,p2)
print(f"Top left is {rect.top_left.x},{rect.top_left.y}")
print(f"Bottom right is {rect.bottom_right.x}, {rect.bottom_right.y}")

# Part 2
#Purpose: Is 1st duration shorter?
#Input: D1, and D2
#Output: T/F

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

duration1 = Duration(3, 40)
duration2 = Duration(2, 30)
print(shorter_duration_than(duration1, duration2))

# Part 3
#Purpose: Which songs are shorter
#Input: list[song], duration
#Output: list[song
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
song1 = Song("Song", "Title1", Duration(2,40))
song2 = Song("Song 2", "Title2",Duration(1, 5))
song3 = Song("Song 3", "Title3",Duration(0, 45))
songs = [song1,song2,song3]
total_duration = Duration (2, 0)
shorter_songs = songs_shorter_than(songs, total_duration)
for song in shorter_songs:
    print(song.title)

# Part 4
#Purpose:Combine times of songs
#Input: list[song]
#Output: list int
class Song:
    def __init__(self, artist: str, title: str, minutes:int, seconds:int):
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
    Song("Song3", "Title3", 2,30),
    Song("Song4", "Title4", 2, 1)
]
playlist = [0,0]
result = running_time(songs, playlist)
print(result)

# Part 5
#Purpose: Make a route
#Input: List list str
#Output: T/F
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
route1 = ['san luis obispo', 'santa margarita', 'atascadero']
print(validate_route(city_links, route1))


# Part 6
#Purpose: Find the longest repetitions of the same value in list
#Input: List int
#Output: list idx
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
list = [1, 1, 2, 2, 1, 1, 1, 3]
print(longest_repetition(list))