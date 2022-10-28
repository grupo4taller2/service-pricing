from sqlalchemy.orm import Session

from src.repositories import BaseRepository
from src.domain.rule import Rule


class RuleRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, rule: Rule):
        pass

    def update(self, rule: Rule):
        pass
