class BasicImageConfig:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_width": ("INT", {
                    "default": 512,
                    "min": 64,
                    "max": 4096,
                    "step": 64,
                    "display": "number"
                }),
                "base_height": ("INT", {
                    "default": 512,
                    "min": 64,
                    "max": 4096,
                    "step": 64,
                    "display": "number"
                }),
                "scale_by": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 4.0,
                    "step": 0.5,
                    "round": 0.1,
                    "display": "number"
                }),
                "batch_size": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 16,
                    "step": 1,
                    "display": "number"
                }),
            }
        }

    CATEGORY = "Configuration"

    RETURN_TYPES = (
        "INT",  # BASE_WIDTH
        "INT",  # BASE_HEIGHT
        "INT",  # SCALED_WIDTH
        "INT",  # SCALED_HEIGHT
        "INT",  # BATCH_SIZE
    )

    RETURN_NAMES = (
        "BASE_WIDTH",
        "BASE_HEIGHT",
        "SCALED_WIDTH",
        "SCALED_HEIGHT",
        "BATCH_SIZE",
    )

    FUNCTION = "build"

    def build(self, base_width, base_height, scale_by, batch_size):
        scaled_width = int(base_width * scale_by)
        scaled_height = int(base_height * scale_by)

        return base_width, base_height, scaled_width, scaled_height, batch_size
