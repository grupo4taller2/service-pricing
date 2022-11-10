from typing import Union

from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from src.domain.rule import Rule


Base = declarative_base()


class RuleDTO(Base):
    __tablename__ = 'pricing_rules'
    id: Union[str, Column] = Column(String, primary_key=True)
    c_trips_last_30m: Union[str, Column] = Column(String)
    c_km: Union[str, Column] = Column(String)
    c_rating: Union[str, Column] = Column(String)
    c_min_price: Union[str, Column] = Column(String)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now())
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), on_update=func.now())

    def to_entity(self):
        return Rule(self.id,
                    self.c_km,
                    self.c_trips_last_30m,
                    self.c_rating,
                    self.c_min_price)

