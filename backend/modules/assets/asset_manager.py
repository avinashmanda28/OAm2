import os
import time


class AssetManager:

    def __init__(self):

        self.assets = []

        # seconds (example: 24 hours)
        self.expiry_time = 86400

    def register_asset(self, path):

        asset = {
            "path": path,
            "created": time.time()
        }

        self.assets.append(asset)

        return asset

    def cleanup_assets(self):

        now = time.time()

        remaining = []

        for asset in self.assets:

            age = now - asset["created"]

            if age > self.expiry_time:

                try:
                    if os.path.exists(asset["path"]):
                        os.remove(asset["path"])
                except Exception:
                    pass

            else:
                remaining.append(asset)

        self.assets = remaining

        return {
            "remaining_assets": len(self.assets)
      }
