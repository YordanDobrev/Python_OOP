from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            current_room = [r for r in self.rooms if room_number == r.number][0]
            guests_in_the_room = current_room.guests
            self.guests -= guests_in_the_room
            current_room.guests -= guests_in_the_room
            current_room.is_taken = False

        except IndexError:
            pass

    def status(self):
        free_rooms = [str(el.number) for el in self.rooms if not el.is_taken]
        taken_rooms = [str(el.number) for el in self.rooms if el.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
