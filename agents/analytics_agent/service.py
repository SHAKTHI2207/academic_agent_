from datetime import datetime
import pandas as pd

class AnalyticsAgent:
    def __init__(self):
        self.role = "Data Analyst"
        self.goal = "Generate insights from evaluation data."

    def generate_report(self, results):
        df = pd.DataFrame(results.get("results", []))
        avg = df["score"].mean() if not df.empty else 0
        insight = "Overall strong performance." if avg > 85 else "Moderate understanding level."
        return {
            "agent": "AnalyticsAgent",
            "average_score": round(avg,2),
            "insight": insight,
            "timestamp": datetime.utcnow().isoformat()
        }

agent = AnalyticsAgent()
def generate_report(results): return agent.generate_report(results)
