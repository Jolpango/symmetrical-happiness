"""
This module handles loading and generation of config files.
"""

import io
import yaml
import printer

CONFIG_PATH = "shlint_config.yaml"

def load_config():
    """Loads config file.
    """
    try:
        with open(CONFIG_PATH, encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)
            printer.config_loaded()
            return config
    except FileNotFoundError:
        return generate_config()

def generate_config():
    """Generates a new config file. If config exist, it will be overwritten
    """
    # Create dictionary with default settings
    # Write to yaml file
    # Return dictionary
    default_cfg = default_config()
    with io.open(CONFIG_PATH, "w", encoding="utf-8") as config_outfile:
        yaml.dump(default_cfg, config_outfile, default_flow_style=False, allow_unicode=True)
        printer.generate_config()
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
