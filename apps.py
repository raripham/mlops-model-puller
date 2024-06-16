import requests
from requests.auth import HTTPBasicAuth
from config import settings
import mlflow
from mlflow import MlflowClient
import logging


def model_puller(modelName, modelAlias):
    mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
    # model = mlflow.search_registered_models(filter_string="name = 'test2' and tag.env like 'prod%'")
    # model = mlflow.search_model_versions(filter_string="name = 'test2' and tag.env like 'prod%'")
    mlclient = MlflowClient()
    model = mlclient.get_model_version_by_alias(name=modelName, alias=modelAlias)
    # print(model.source, model.status, "\n", model)
    test_model = mlclient.get_registered_model(name=modelName)
    # print(test_model.aliases.keys())
    fil_key = filter(lambda x: x.startswith("prod-"), test_model.aliases.keys())
    print(list(fil_key)[0])
    # model_url = f"{settings.MLFLOW_TRACKING_URI}/api/2.0/mlflow/registered-models/alias?name={modelName}&alias={modelAlias}"

    # response = requests.get(
    #     url=model_url, 
    #     auth=HTTPBasicAuth(settings.MLFLOW_TRACKING_USERNAME, settings.MLFLOW_TRACKING_PASSWORD)
    # )

    # response_json = response.json()
    # modelVersion = response_json["model_version"]["version"]
    # modelPath = response_json["model_version"]["source"]

    logging.info("Downloading model %s:%s from path %s", modelName, model.version, model.source)
    print(f"Downloading model {modelName}:{model.version} from path {model.source}")

    return model.source, model.version

def download_model(modelName, modelAlias):
    modelPath, modelVersion = model_puller(modelName, modelAlias)
    mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
    try:
        # mlflow.artifacts.download_artifacts(artifact_uri=modelPath, dst_path="./model")
        print(f"Download model {modelName}:{modelVersion} successfully!")
    except IOError as e:
        logging.error('Error occurred ' + str(e))