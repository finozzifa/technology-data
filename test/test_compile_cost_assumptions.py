#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("./scripts")

from test.conftest import get_config_dict
from compile_cost_assumptions import add_atb_electricity_data

def test_gadd_atb_electricity_data():
