import random


class ExperimentEngine:

    def __init__(self):
        self.history = []

    def generate_variations(self, script):

        variations = []

        for i in range(3):

            modified_script = script + f"\n\nVariation {i+1}: stronger storytelling."

            variations.append(modified_script)

        return variations

    def score_variation(self, script):

        score = random.uniform(5, 10)

        return score

    def run_experiments(self, script):

        variations = self.generate_variations(script)

        results = []

        for var in variations:

            score = self.score_variation(var)

            results.append({
                "script": var,
                "score": score
            })

        best = max(results, key=lambda x: x["score"])

        experiment_report = {
            "variations_tested": len(results),
            "best_score": best["score"],
            "best_script": best["script"]
        }

        self.history.append(experiment_report)

        return experiment_report
