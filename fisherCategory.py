import enum
from typing import List


class FisherCategory(enum.Enum):
    Newbie = 1
    Amateur = 2
    Professional = 3

    def getCategories() -> List[str]:
        return [e.name for e in FisherCategory]
