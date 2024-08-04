from dataclasses import dataclass
from enum import IntEnum, StrEnum, auto
from typing import Literal


class Gender(StrEnum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()


class Element(StrEnum):
    LIGHTNING = auto()
    FIRE = auto()
    WIND = auto()
    PHYSICAL = auto()
    ICE = auto()
    QUANTUM = auto()
    IMAGINARY = auto()


class Path(StrEnum):
    DESTRUCTION = "The Destruction"
    HARMONY = "The Harmony"
    HUNT = "The Hunt"
    ABUNDANCE = "The Abundance"
    PRESERVATION = "The Preservation"
    NIHILITY = "The Nihility"
    ERUDITION = "The Erudition"


class Height(StrEnum):
    SHORT = auto()
    MEDIUM = auto()
    TALL = auto()


class Looks(StrEnum):
    COVERED_UP = auto()
    CASUAL = auto()
    REVEALING = auto()


class Rarity(IntEnum):
    FIVE_STAR = 5
    FOUR_STAR = 4


@dataclass(slots=True)
class Version:
    major: int
    minor: int

    def __str__(self):
        return f"{self.major}.{self.minor}"

    @classmethod
    def parse(cls, version: str):
        major, minor = version.split(".")
        return cls(int(major), int(minor))


@dataclass(slots=True)
class BannerPhase:
    version: Version
    phase: Literal[1, 2]

    def __str__(self):
        return f"{self.version}/{self.phase}"

    @classmethod
    def parse(cls, banner_phase: str):
        version, phase = banner_phase.split("/")
        phase = int(phase)
        if phase != 1 and phase != 2:
            raise ValueError("Invalid phase")

        return cls(Version.parse(version), phase)

    @classmethod
    def try_parse(cls, banner_phase: str):
        try:
            return cls.parse(banner_phase)
        except ValueError:
            return None


@dataclass(slots=True)
class Character:
    name: str
    gender: Gender
    element: Element
    path: Path
    rating: Rarity
    first_run: BannerPhase | None
    height: str
    looks: str

    def csv_line(self) -> str:
        """Serialize the character into a CSV line.

        The CSV line will be in the following format:

        `name,gender,element,path,rating,first_run,height,looks`

        Returns:
            str: The CSV line.
        """
        first_run = str(self.first_run) if self.first_run else "-"

        return f"{self.name},{self.gender},{self.element},{self.path},{self.rating},{first_run},{self.height},{self.looks}"

    @classmethod
    def from_csv_line(cls, line: str, separator: str = ",") -> "Character":
        """Parse a CSV line into a character.

        The CSV line should be in the following format:

        `name,gender,element,path,rating,first_run,height,looks`

        Args:
            line (str): The CSV line.

        Returns:
            Character: The parsed character.
        """

        columns = line.strip()

        name = columns[0]
        gender = Gender(columns[1])
        element = Element(columns[2])
        path = Path(columns[3])
        rating = Rarity(int(columns[4]))
        first_run = BannerPhase.try_parse(columns[5])
        height = Height(columns[6])
        looks = Looks(columns[7])

        return cls(name, gender, element, path, rating, first_run, height, looks)
