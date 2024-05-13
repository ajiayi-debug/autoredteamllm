import transformers
import torch
from config import huggingface_model,uri

model_id = huggingface_model

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)
pipeline("Hey how are you doing today?")

#will work on this if i get a gpu. 