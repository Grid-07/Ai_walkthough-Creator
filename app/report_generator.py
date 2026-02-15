from transformers import pipeline

class ReportGenerator:

    def __init__(self):
        self.generator = None

    def _load_model(self):
        if self.generator is None:
            self.generator = pipeline(
                "text-generation",
                model="google/flan-t5-small"
            )

    def generate(self, floor_plan, warnings, geometry):
        self._load_model()

        summary = f"""
You are a senior system architect reviewing a floor plan.

Rooms:
{floor_plan['rooms']}

Feasibility Warnings:
{warnings}

Generate a structured technical architectural walkthrough with:
- Overview
- Structural Analysis
- Risk Assessment
- Optimization Suggestions
"""

        output = self.generator(summary, max_length=300, do_sample=False)

        return output[0]["generated_text"]
