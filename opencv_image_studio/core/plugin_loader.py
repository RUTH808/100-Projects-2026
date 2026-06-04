import os
import importlib


class PluginLoader:

    def __init__(self):

        self.plugins = {}

    def load_plugins(self):

        plugin_folder = "plugins"

        for file in os.listdir(
            plugin_folder
        ):

            if (
                not file.endswith(".py")
                or
                file.startswith("__")
            ):
                continue

            module_name = file[:-3]

            module = (
                importlib.import_module(
                    f"plugins.{module_name}"
                )
            )

            self.plugins[
                module.PLUGIN_NAME
            ] = module

        return self.plugins