from abc import ABC, abstractmethod
from Resume_generator.user_info_module.Persone import Persone
class Convertor(ABC): # basic class for inheriting
    @abstractmethod
    def convert(self, persone:Persone, file_path:str):
        pass
   