from pydantic import BaseModel, validator
import pandas as pd
from dataclasses import dataclass


class Excel_data(BaseModel):
    pass


@dataclass
class Rank:
    pass


class Reader:
    def __init__(self) -> None:
        pass

    def read_excel(self, file: str) -> pd.Dataframe:
        return NotImplemented
