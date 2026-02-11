from .basic_image_config import BasicImageConfig

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BasicImageConfig": BasicImageConfig,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "BasicImageConfig": "Basic Image Config",
}

WEB_DIRECTORY = "./src/web"
