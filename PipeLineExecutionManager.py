# Design Bioinformatics Execution system
# System simulates execution of bioinformatics pipeline, tracks their state and allows inspection of the results

# 3 steps : QC,Alignment and VC
# BaseClass: PipelineManager

class PipelineStep:
    def __init__(self,name,status,duration):
        self.name = name
        if status not in ("PENDING", "RUNNING", "COMPLETED","FAILED"):
            raise ValueError(f"Status: {status} is not valid!")
        self._status = status

        if duration < 0:
            raise ValueError(f"Selected duration is invalid!")
        self.duration = duration


    def execute(self):
        if self._status == "PENDING":
            self._status = "COMPLETED"


class QualityControl(PipelineStep):  
    def __init__(self,status_score,name,status,duration):
        super().__init__(name,status,duration)
        self.score = status_score

    def execute(self):
        if self.score > 81:
            super().execute()
        else:
            self._status = "FAILED"

class Alignment(PipelineStep):
    def __init__(self):
        pass
    def execute(self):
        super().execute()

class VariantCalling(PipelineStep):
    def __init__(self):
        pass


    def execute(self):
        super().execute()


class Pipeline:
    steps = []
    def __init__(self,run_id):
        self.run_id = run_id

    def add_step(self):


if __name__ == "__main__":
    pipe = Pipeline("RUN_01",'s')
    pipe.add_step(QualityControl(34))

