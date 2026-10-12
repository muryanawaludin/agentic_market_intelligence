"""
Konfigurasi Global Sistem Intelijen Pasar Finansial.
© 2026 Muryan Awaludin.
"""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SystemConfig:
    APP_TITLE: str = "Market Intelligence Agent: Reasoning Engine"
    AUTHOR_COPYRIGHT: str = "© 2026 Muryan Awaludin. Seluruh hak cipta dilindungi."
    DATA_PATH: str = os.path.join(os.path.dirname(__file__), "data", "all-data.csv")
    MAX_REACT_STEPS: int = 4
    MAX_REFLEXION_TRIALS: int = 2
    TOT_BRANCHING_FACTOR: int = 2
    TOT_MAX_DEPTH: int = 2

CONFIG = SystemConfig()