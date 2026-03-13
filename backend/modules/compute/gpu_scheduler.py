class GPUScheduler:

    def __init__(self):

        self.current_jobs = []

    def schedule_job(self, job):

        self.current_jobs.append(job)

        return {
            "status": "scheduled",
            "job_id": len(self.current_jobs)
        }

    def list_jobs(self):

        return self.current_jobs
