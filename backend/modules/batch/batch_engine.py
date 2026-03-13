class BatchEngine:

    def __init__(self):
        pass

    def create_batch(self, prompts):

        jobs = []

        for prompt in prompts:

            jobs.append({
                "prompt": prompt,
                "status": "queued"
            })

        return jobs
