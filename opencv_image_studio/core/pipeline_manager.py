import json


class PipelineManager:

    def __init__(self):

        self.pipeline = []

    def add_step(
        self,
        plugin_name,
        params
    ):

        self.pipeline.append({

            "plugin":
                plugin_name,

            "params":
                params
        })

    def remove_step(
        self,
        index
    ):

        if (
            index is not None
            and
            0 <= index <
            len(self.pipeline)
        ):

            self.pipeline.pop(index)

    def move_up(
        self,
        index
    ):

        if (
            index is not None
            and
            index > 0
        ):

            self.pipeline[index], \
            self.pipeline[index - 1] = \
            self.pipeline[index - 1], \
            self.pipeline[index]

    def move_down(
        self,
        index
    ):

        if (
            index is not None
            and
            index <
            len(self.pipeline)-1
        ):

            self.pipeline[index], \
            self.pipeline[index + 1] = \
            self.pipeline[index + 1], \
            self.pipeline[index]

    def clear(self):

        self.pipeline.clear()

    def save(
        self,
        filepath
    ):

        with open(
            filepath,
            "w"
        ) as f:

            json.dump(
                self.pipeline,
                f,
                indent=4
            )

    def load(
        self,
        filepath
    ):

        with open(
            filepath,
            "r"
        ) as f:

            self.pipeline = (
                json.load(f)
            )

    def execute(
        self,
        img,
        plugins
    ):

        result = img.copy()

        for step in self.pipeline:

            plugin_name = (
                step["plugin"]
            )

            params = (
                step["params"]
            )

            plugin = plugins[
                plugin_name
            ]

            result = plugin.process(
                result,
                params
            )

        return result