from typing import Union

from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

from src.domain.rule import Rule

Base = declarative_base()


class RuleDTO(Base):
    __tablename__ = 'rules'
    id: Union[str, Column] = Column(String, primary_key=True)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now())
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), on_update=func.now())
