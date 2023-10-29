import os
import openai
from gpttuner.GPTTuner import GPTTuner

tuner: GPTTuner = GPTTuner(os.environ["OPENAI_KEY"])

print(tuner.ListJobs())
