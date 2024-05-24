from typing import Dict, List, Union
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import input  # Import the data module
from config import location, endpoint, project
def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str,
    api_endpoint: str = "asia-southeast1-aiplatform.googleapis.com",
):
    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    instances = instances if isinstance(instances, list) else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    # print("response")
    # print(" deployed_model_id:", response.deployed_model_id)
    
    # Handling the response
    predictions = response.predictions
    for prediction in predictions:
        print(prediction)
    
    # # Printing additional fields if they exist
    # if hasattr(response, 'model'):
    #     print(" model:", response.model)
    # if hasattr(response, 'model_display_name'):
    #     print(" model_display_name:", response.model_display_name)
    # if hasattr(response, 'model_version_id'):
    #     print(" model_version_id:", response.model_version_id)

# Use the imported data from the module
predict_custom_trained_model_sample(
    project=project,
    endpoint_id=endpoint,
    location=location,
    api_endpoint=location+"-aiplatform.googleapis.com",
    instances=input.data['instances']  # Access the data from the imported module
)
