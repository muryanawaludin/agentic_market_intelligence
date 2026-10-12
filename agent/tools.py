"""
Pustaka Perkakas Finansial untuk Verifikasi Data Pasar.
© 2026 Muryan Awaludin.
"""
import json

class FinancialToolRegistry:
    
    @staticmethod
    def get_market_telemetry(ticker_or_sector: str) -> str:
        """Mengambil indikator makro dan teknikal terkini emiten atau sektor terkait."""
        ticker = ticker_or_sector.upper()
        mock_data = {
            "PROFIT": {"pe_ratio": 16.4, "momentum_rsi": 62.5, "guidance": "UPWARD", "analyst_rating": "BUY"},
            "LOSS": {"pe_ratio": 34.1, "momentum_rsi": 28.0, "guidance": "DOWNWARD", "analyst_rating": "STRONG_SELL"},
            "FLAT": {"pe_ratio": 20.1, "momentum_rsi": 50.2, "guidance": "NEUTRAL", "analyst_rating": "HOLD"}
        }
        
        if "PROFIT" in ticker or "ROSE" in ticker or "DIVIDEND" in ticker:
            return json.dumps(mock_data["PROFIT"])
        elif "LOSS" in ticker or "REDUCTION" in ticker:
            return json.dumps(mock_data["LOSS"])
        return json.dumps(mock_data["FLAT"])

    @staticmethod
    def calculate_valuation_impact(metric_name: str, change_percentage: float) -> str:
        """Menghitung dampak estimasi valuasi terhadap arus kas terdiskon (DCF)."""
        impact_multiplier = 1.25 if metric_name.lower() == "profit" else 0.8
        projected_shift = change_percentage * impact_multiplier
        return json.dumps({
            "metric": metric_name,
            "projected_valuation_impact_percent": round(projected_shift, 2),
            "confidence_interval": "95%"
        })

    @classmethod
    def execute(cls, tool_name: str, **kwargs) -> str:
        if tool_name == "get_market_telemetry":
            return cls.get_market_telemetry(**kwargs)
        elif tool_name == "calculate_valuation_impact":
            return cls.calculate_valuation_impact(**kwargs)
        return json.dumps({"error": f"Tool '{tool_name}' tidak ditemukan."})