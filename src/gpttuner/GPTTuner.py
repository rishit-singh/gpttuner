import openai

class TuningJob:
    def __init__(self, _id: str, trainingFileID: str):
        self.ID: str = _id
        self.TrainingFileID: str = trainingFileID
    def ToDict(self):
        return 

class GPTTuner:
    def CreateTrainingFile(self, filePath: str) -> dict:
        response: dict = {}
        
        try:
            response = openai.File.create(file=open(filePath, "rb"))
        except Exception as e:
            print(e.args[1])

        return response

    def CreateJob(self, trainingFile: str) -> dict[str, str]:
        response: dict = openai.FineTuningJob.create(model=self.Model, training_file=trainingFile)

        return response
        
    def __init__(self, apiKey: str, model: str = "gpt3.5-turbo"):
        self.Model: str = model
        self.APIKey: str = apiKey
