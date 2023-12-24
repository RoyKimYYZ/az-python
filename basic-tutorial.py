# https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world
import os
import numpy as np

# environment variables

for key, value in os.environ.items():
    print(f"{key}: {value}")
print(os.environ["AZURE_OPENAI_ENDPOINT"])
os.environ['AZURE_SUBSCRIPTION_ID'] = ""
print(os.environ["AZURE_SUBSCRIPTION_ID"])


# random number
print(np.random.randint(1,9))

