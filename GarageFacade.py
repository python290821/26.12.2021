from DbRepo import DbRepo
from sqlalchemy import text
from Car import Car
from db_config import local_session, create_all_entities

repo = DbRepo(local_session)
class GarageFacade:
    def add_car(self, car):
        repo.add(car)


