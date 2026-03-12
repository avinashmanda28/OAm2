class PluginManager:

    def __init__(self):

        self.plugins = {}

    def register_plugin(self, name, plugin):

        self.plugins[name] = plugin

        return {
            "plugin_registered": name
        }

    def get_plugin(self, name):

        return self.plugins.get(name)

    def list_plugins(self):

        return {
            "total_plugins": len(self.plugins),
            "plugins": list(self.plugins.keys())
        }

    def remove_plugin(self, name):

        if name in self.plugins:

            del self.plugins[name]

            return {
                "removed": name
            }

        return {
            "error": "plugin_not_found"
      }
