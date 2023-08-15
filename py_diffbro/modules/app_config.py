# config_manager.py

import os
from pathlib import Path
import yaml


class ConfigManager:
    """
    A simple configuration manager for reading and updating YAML configuration files.

    Usage Example:
    --------------
    ```python
    manager = ConfigManager('myapp')

    # Read configuration
    current_config = manager.read_config()
    print("Current Config:", current_config)

    # Update configuration
    new_data = {"key": "value"}
    manager.update_config(new_data)

    # Read the updated configuration
    updated_config = manager.read_config()
    print("Updated Config:", updated_config)
    ```
    """

    def __init__(self, app_name):
        self.config_dir = Path.home() / f".{app_name}"
        self.config_path = self.config_dir / "config.yml"
        self._ensure_config_dir_exists()

    def _ensure_config_dir_exists(self):
        """Ensure the configuration directory exists."""
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # If the config file doesn't exist, create an empty one
        if not self.config_path.exists():
            with open(self.config_path, "w") as file:
                yaml.safe_dump({}, file)

    def read_config(self):
        """Read the configuration and return as a dictionary."""
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)

    def update_config(self, new_config):
        """Update the configuration with the provided dictionary."""
        with open(self.config_path, "w") as file:
            yaml.safe_dump(new_config, file)
