import yaml
import os




path=os.path.join(os.getcwd(),"config\config.yaml")



def load_config(config_path: str=path)->dict:
    with open(config_path,"r")as file:
        config=yaml.safe_load(file)

    return config 

