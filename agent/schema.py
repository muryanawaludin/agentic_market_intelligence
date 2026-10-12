"""
Definisi Skema Data untuk Pola Penalaran Agen.
© 2026 Muryan Awaludin.
"""
from typing import List, Dict, Any, Optional, Literal
from pydantic import BaseModel, Field

class NewsItem(BaseModel):
    sentence: str
    ground_truth_sentiment: Optional[str] = None

class ReActStep(BaseModel):
    step_number: int
    thought: str
    action: str
    action_input: Dict[str, Any]
    observation: str

class ReflexionTrial(BaseModel):
    trial_number: int
    initial_analysis: str
    critique_score: float
    reflection: str
    refined_analysis: str

class ThoughtNode(BaseModel):
    node_id: str
    depth: int
    hypothesis: str
    evaluation_score: float
    status: Literal["EXPLORED", "PRUNED", "SELECTED"]
    children: List['ThoughtNode'] = Field(default_factory=list)

class ReasoningComparisonResult(BaseModel):
    news_text: str
    react_steps: List[ReActStep]
    react_verdict: str
    reflexion_trials: List[ReflexionTrial]
    reflexion_verdict: str
    tot_tree: ThoughtNode
    tot_verdict: str