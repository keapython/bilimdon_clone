
from typing import Optional

from datetime import datetime, date, timezone, time

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, DateTime, Date, Integer




from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique= True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32), unique= True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate: Mapped[date] = mapped_column(Date)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)


class Participation(Base):
    __tablename__ = "participations"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    game_id: Mapped[int] = mapped_column()
    start_time: Mapped[time]
    end_time: Mapped[Optional[time]] = mapped_column(nullable=True)
    gained_score: Mapped[int] = mapped_column(default=0)
    registered_at: Mapped[datetime]


class Game(Base):
    __tablename__ = "games"

    id:Mapped[int] = mapped_column(primary_key=True)

    owner_id:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=True

    )
    owner:Mapped[Optional["User"]] = relationship("User")
    topic_id:Mapped[int] = mapped_column()

