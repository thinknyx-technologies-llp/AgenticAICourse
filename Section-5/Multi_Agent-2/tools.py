from crewai.tools import BaseTool

class CustomerSupportDataTool(BaseTool):
    name: str = "Customer Support Data Fetcher"
    description: str = (
      "Fetches recent customer support interactions, tickets, and feedback. "
      "Returns a summary string.")

      # YOUR COMPANY LOGIC

    def _run(self, argument: str) -> str:
        print(f"--- Fetching data for query: {argument} ---")
        return (
            """Recent Support Data Summary:
- 50 tickets related to 'login issues'. Avg resolution: 48h
- 30 tickets about 'billing discrepancies'. Avg resolution: 12h
- 20 feature request tickets. Many closed without resolution.
- Frequent feedback: 'confusing UI' for password reset.
- High volume calls on 'account verification'.
- Sentiment: growing frustration with login issue delays.
- Agents report difficulty reproducing login issues."""
        )
