class TextPreview:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True, "multiline": True})
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO", "unique_id": "UNIQUE_ID"},
        }

    CATEGORY = "Tools:TextPreviewMultiline"
    OUTPUT_NODE = True

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "doit"

    def doit(self, text, prompt=None, extra_pnginfo=None, unique_id=None):
        return {"ui": {"string": [text, unique_id, ]}, "result": (text, unique_id,)}

NODE_CLASS_MAPPINGS = {
    "Tools:TextPreview": TextPreview,
}

# 节点名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "Tools:TextPreview": "TextPreview 🅜🅒",
}
