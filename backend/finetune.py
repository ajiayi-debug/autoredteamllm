from pymongo import MongoClient
from config import uri  # Make sure this module correctly provides the MongoDB URI
from groq import Groq
#create another database. This temporarily stores current data to finetune. We will delete after finetuning.
# Connect to MongoDB
client = MongoClient(uri)
db = client['all_finetune_data']  
collection = db['finetune_all']  

# Find documents in the collection
documents = collection.find({}) 

for doc in documents:
    label = doc.get('label', 'Default Label')  
    content = doc.get('content', 'No Content Available')
    data = {
        "content": content,
        "label": label  
    }
    collection_new=db['finetune']
    result = collection_new.insert_one(data)
    print("Data inserted with id:", result.inserted_id)

#we will now use google collab to finetune Llama 3 8b as a demo and to see if our blue team efforts has worked. This dataset ('finetune') will be deleted after finetuning is complete. In future, I would like to ask an LLM to create variations of attack prompts for more finetuning data.
    



