#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import pytest
import yaml


@pytest.fixture(scope="function")
def get_config_dict():
    path_config = pathlib.Path(pathlib.Path.cwd(), "config.yaml")
    with open(path_config, "r") as file:
        config_dict = yaml.safe_load(file)
    return config_dict
