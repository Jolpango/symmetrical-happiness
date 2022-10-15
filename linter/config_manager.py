"""
This module handles loading and generation of config files.
"""

import yaml
import io

config_path = "shlint_config.yaml"

def load_config():
    """Loads config file.
    """
    try:
        with open(config_path) as config_file:
            config = yaml.safe_load(config_file)
            return config
    except:
        return generate_config()

def generate_config():
    """Generates a new config file. If config exist, it will be overwritten
    """
    # Create dictionary with default settings
    # Write to yaml file
    # Return dictionary
    default_cfg = default_config()
    with io.open(config_path, "w", encoding="utf-8") as config_outfile:
        yaml.dump(default_cfg, config_outfile, default_flow_style=False, allow_unicode=True)
    return default_cfg

def default_config():
    """Returns default config
    """
    # Create dictionary with default settings
    # Return dictionary
    default_cfg = {
        "formatting" : {
            "comments" : { "spaces": 1 },
            "indentation" : { "spaces": 4, "excluded_blocks": ["document", "verbatim"] },
            "blank_lines" : { "nr": 1 },
            "git_support": { "newline_after_sentence": True }
        },
        "overwrite": False
    }
    return default_cfg