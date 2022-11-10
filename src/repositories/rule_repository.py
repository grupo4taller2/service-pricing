from sqlalchemy.orm import Session

from src.repositories.base_repository import BaseRepository
from src.domain.rule import Rule
from src.database.rule_dto import RuleDTO


class RuleRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, rule: Rule):
        pass

    def update(self, rule: Rule):
        pass

    def all(self):
        rules_dtos = self.session.query(RuleDTO)
