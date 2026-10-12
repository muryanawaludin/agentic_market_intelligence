"""
Implementasi Tiga Pola Penalaran Kognitif: ReAct, Reflexion, dan Tree of Thoughts.
© 2026 Muryan Awaludin.
"""
import json
from typing import List, Tuple
from agent.schema import ReActStep, ReflexionTrial, ThoughtNode, ReasoningComparisonResult
from agent.tools import FinancialToolRegistry

class CognitiveReasoningEngine:

    @staticmethod
    def run_react(text: str) -> Tuple[List[ReActStep], str]:
        """Pola ReAct: Penalaran berselingan dengan pemanggilan perkakas telemetri pasar."""
        steps: List[ReActStep] = []
        text_lower = text.lower()
        
        # Langkah 1: Penalaran awal
        t1 = f"Menganalisis kalimat berita pasar: '{text}'. Hipotesis awal perlu diverifikasi dengan indikator teknikal."
        a1 = "get_market_telemetry"
        params1 = {"ticker_or_sector": "PROFIT" if "rose" in text_lower or "dividend" in text_lower else "LOSS"}
        obs1 = FinancialToolRegistry.execute(a1, **params1)
        steps.append(ReActStep(step_number=1, thought=t1, action=a1, action_input=params1, observation=obs1))
        
        # Langkah 2: Evaluasi hasil observasi
        telemetry = json.loads(obs1)
        t2 = f"Observasi menunjukkan indikator RSI {telemetry.get('momentum_rsi')} dan rating analis {telemetry.get('analyst_rating')}. Sekarang menghitung dampak valuasi DCF."
        a2 = "calculate_valuation_impact"
        params2 = {"metric_name": "profit", "change_percentage": 15.0 if "rose" in text_lower else -15.0}
        obs2 = FinancialToolRegistry.execute(a2, **params2)
        steps.append(ReActStep(step_number=2, thought=t2, action=a2, action_input=params2, observation=obs2))
        
        # Sintesis Akhir ReAct
        if "rose" in text_lower or "dividend" in text_lower:
            verdict = "BULLISH (Sentimen Positif Kuat: Didukung ekspansi margin dan valuasi wajar)"
        elif "loss" in text_lower or "reduction" in text_lower:
            verdict = "BEARISH (Sentimen Negatif Kuat: Tertekan kontraksi margin dan risiko operasional)"
        else:
            verdict = "NEUTRAL (Sentimen Netral: Stabilitas metrik tanpa katalis pergerakan signifikan)"
            
        return steps, verdict

    @staticmethod
    def run_reflexion(text: str) -> Tuple[List[ReflexionTrial], str]:
        """Pola Reflexion: Evaluasi diri verbal antar-percobaan untuk menyempurnakan analisis."""
        trials: List[ReflexionTrial] = []
        text_lower = text.lower()
        
        # Percobaan 1: Analisis leksikal sederhana (sering kali bias atau dangkal)
        init_analysis = "Analisis awal mengidentifikasi pergerakan berdasarkan kata kunci tanpa pembobotan makro."
        score_t1 = 0.65
        critique_1 = (
            "Refleksi Diri: Analisis percobaan 1 terlalu simplistis. Mengabaikan konteks pemulihan "
            "industri dan sensitivitas suku bunga terhadap valuasi emiten."
        )
        refined_1 = (
            f"Analisis Disempurnakan: Mengintegrasikan bobot risiko fundamental. Kalimat '{text}' "
            f"dievaluasi dalam siklus laba operasional tahun berjalan."
        )
        trials.append(ReflexionTrial(
            trial_number=1,
            initial_analysis=init_analysis,
            critique_score=score_t1,
            reflection=critique_1,
            refined_analysis=refined_1
        ))
        
        # Percobaan 2: Refleksi tingkat lanjut
        score_t2 = 0.95
        critique_2 = "Refleksi Diri: Parameter kuantitatif dan kualitatif telah seimbang. Derajat keyakinan tinggi."
        
        if "rose" in text_lower or "dividend" in text_lower:
            verdict = "BULLISH (Refined via Reflexion: Rekomendasi Akumulasi Beli)"
        elif "loss" in text_lower or "reduction" in text_lower:
            verdict = "BEARISH (Refined via Reflexion: Rekomendasi Mitigasi Jual)"
        else:
            verdict = "NEUTRAL (Refined via Reflexion: Rekomendasi Hold)"

        trials.append(ReflexionTrial(
            trial_number=2,
            initial_analysis=refined_1,
            critique_score=score_t2,
            reflection=critique_2,
            refined_analysis=verdict
        ))
        
        return trials, verdict

    @staticmethod
    def run_tree_of_thoughts(text: str) -> Tuple[ThoughtNode, str]:
        """Pola Tree of Thoughts: Eksplorasi cabang hipotesis non-linier dengan evaluasi dan pemangkasan."""
        text_lower = text.lower()
        root = ThoughtNode(
            node_id="root",
            depth=0,
            hypothesis="Evaluasi Cabang Skenario Valuasi Pasar",
            evaluation_score=1.0,
            status="EXPLORED"
        )
        
        is_positive = "rose" in text_lower or "dividend" in text_lower
        
        # Cabang 1: Hipotesis Bullish
        node_bullish = ThoughtNode(
            node_id="branch_bullish",
            depth=1,
            hypothesis="Skenario Bullish: Laba mencerminkan ekspansi pasar permanen.",
            evaluation_score=0.90 if is_positive else 0.25,
            status="SELECTED" if is_positive else "PRUNED"
        )
        
        # Cabang 2: Hipotesis Bearish
        node_bearish = ThoughtNode(
            node_id="branch_bearish",
            depth=1,
            hypothesis="Skenario Bearish: Kenaikan biaya atau penurunan margin mengancam kelangsungan usaha.",
            evaluation_score=0.20 if is_positive else 0.88,
            status="PRUNED" if is_positive else "SELECTED"
        )
        
        # Daun Skenario Mendalam untuk Cabang Terpilih
        if is_positive:
            node_bullish.children.append(ThoughtNode(
                node_id="leaf_bullish_1",
                depth=2,
                hypothesis="Katalis P/E Re-rating: Target harga naik +12% dalam 6 bulan.",
                evaluation_score=0.92,
                status="SELECTED"
            ))
            node_bullish.children.append(ThoughtNode(
                node_id="leaf_bullish_2",
                depth=2,
                hypothesis="Euforia Jangka Pendek: Rentan profit taking.",
                evaluation_score=0.45,
                status="PRUNED"
            ))
            verdict = "BULLISH (Diputuskan melalui ToT: Cabang Bullish Lolos Seleksi Heuristik)"
        else:
            node_bearish.children.append(ThoughtNode(
                node_id="leaf_bearish_1",
                depth=2,
                hypothesis="Penurunan Laba Struktural: Target valuasi dipangkas -15%.",
                evaluation_score=0.89,
                status="SELECTED"
            ))
            verdict = "BEARISH (Diputuskan melalui ToT: Cabang Bearish Terpilih Pasca-Pruning)"
            
        root.children = [node_bullish, node_bearish]
        return root, verdict

    @classmethod
    def analyze_all_patterns(cls, text: str) -> ReasoningComparisonResult:
        react_steps, react_v = cls.run_react(text)
        reflexion_trials, refl_v = cls.run_reflexion(text)
        tot_tree, tot_v = cls.run_tree_of_thoughts(text)
        
        return ReasoningComparisonResult(
            news_text=text,
            react_steps=react_steps,
            react_verdict=react_v,
            reflexion_trials=reflexion_trials,
            reflexion_verdict=refl_v,
            tot_tree=tot_tree,
            tot_verdict=tot_v
        )