"""
ai-architecture-template - test_notebooks.py

Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
import papermill as pm
from azure_utils.machine_learning.utils import load_configuration


def test_00_aml_configuration():
    cfg = load_configuration("../workspace_conf.yml")

    subscription_id = cfg['subscription_id']
    resource_group = cfg['resource_group']
    workspace_name = cfg['workspace_name']
    workspace_region = cfg['workspace_region']

    results = pm.execute_notebook(
        '../notebooks/00_AMLConfiguration.ipynb',
        '../notebooks/00_AMLConfiguration_Output.ipynb',
        parameters=dict(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name,
                        workspace_region=workspace_region)
    )

    assert results is not None
