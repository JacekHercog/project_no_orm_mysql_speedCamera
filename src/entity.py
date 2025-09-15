from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Self, override, Any

@dataclass
class Entity(ABC):
    """Base class for all entities."""
    id_: int | None = None

    @classmethod    
    @abstractmethod
    def from_row(cls, *args: Any) -> Self:
        """Convert a database row to an entity."""
        pass


@dataclass
class SpeedCamera(Entity):
    """Base class for speed cameras."""
    location: str | None = None
    allowed_speed: int | None = None

    @classmethod    
    @override
    def from_row(cls, *args: Any) -> Self:
        """Convert a database row to a speed camera."""
        return cls(
            id_=int(args[0]),
            location=args[1],
            allowed_speed=int(args[2]) 
        )

@dataclass
class Driver(Entity):
    """Base class for drivers"""
    first_name: str | None = None
    last_name: str | None = None
    registration_number: str | None = None

    @classmethod
    @override
    def from_row(cls, *args: Any) -> Self:
        """Convert a database row to a driver."""
        return cls(
            id_=int(args[0]),
            first_name=args[1],
            last_name=args[2],
            registration_number=args[3]
        )
    
@dataclass
class Offense(Entity):
    """Base class for offences."""
    description: str | None = None  
    penalty_points: int | None = None
    fine_amount: int | None = None

    @classmethod
    @override
    def from_row(cls, *args: Any) -> Self:
        """Convert a database row to an offence."""
        return cls(
            id_=int(args[0]),
            description=args[1],
            penalty_points=int(args[2]),
            fine_amount=int(args[3])
        )

@dataclass
class Violation(Entity):
    """Base class for violations."""
    violation_date: str | None = None  # YYYY-MM-DD format
    driver_id: int | None = None
    speed_camera_id: int | None = None
    offence_id: int | None = None

    @classmethod
    @override
    def from_row(cls, *args: Any) -> Self:
        """Convert a database row to a violation."""
        return cls(
            id_=int(args[0]),
            violation_date=args[1],
            driver_id=int(args[2]),
            speed_camera_id=int(args[3]),
            offence_id=int(args[4])
        )