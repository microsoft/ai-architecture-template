"""
ai-architecture-template - test_notebooks.py

Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
import papermill as pm
from azure_utils.machine_learning.utils import load_configuration
from junit_xml import TestSuite, TestCase


def test_00_aml_configuration(capsys):
    cfg = load_configuration("../workspace_conf.yml")

    subscription_id = cfg['subscription_id']
    resource_group = cfg['resource_group']
    workspace_name = cfg['workspace_name']
    workspace_region = cfg['workspace_region']

    results = pm.execute_notebook(
        'notebooks/00_AMLConfiguration.ipynb',
        'notebooks/00_AMLConfiguration.output_ipynb',
        parameters=dict(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name,
                        workspace_region=workspace_region),
        kernel_name="ai-architecture-template"
    )

    for cell in results.cells:
        if cell.cell_type is "code":
            assert not cell.metadata.papermill.exception, "Error in Python Notebook"

    regex = r'Deployed (.*) with name (.*) seconds.'

    captured = capsys.readouterr()
    output = captured.out

    import re
    searchObj = re.findall(regex, output)

    test_cases = []

    for group in searchObj:
        test_cases += TestCase(name=group(1), classname='some.class.name', elapsed_sec=group(2), stdout=group(),
                               status="Success")

    ts = TestSuite("my test suite", test_cases)

    with open('timing-test-output.xml', 'w') as f:
        TestSuite.to_file(f, [ts], prettyprint=False)
