"""
This module handles loading and generation of config files.
"""

config_path = "shlint_config.yaml"

def load_config():
    """Loads config file.
    """
    try:
        with open(config_path) as f:
            return {"config": "config"}
    except:
        return generate_config()

def generate_config():
    """Generates a new config file. If config exist, it will be overwritten
    """
    # Create dictionary with default settings
    # Write to yaml file
    # Return dictionary