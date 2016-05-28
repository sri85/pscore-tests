"""
Configuration file
"""

import os


GOUSTO_HEALTHY_RECIPE_PAGE = 'https://www.gousto.co.uk/this-weeks-recipes'

RUN_LOCAL = 'local'
CHROME = 'chrome'
FIREFOX = 'firefox'


def set_environment_variables(values):
    for variable_name, variable_value in values.items():
        # will not attempt to set a blank variable value
        if variable_value:
            set_environment_variable(variable_name, variable_value)


def get_environment_variable(name):
    return os.getenv(name)


def set_environment_variable(name, value):
    os.environ[name] = str(value)


user_local_settings = dict(PSCORE_SCREENSHOT_DIR=os.path.join(os.getcwd(), 'screenshots'),
                           PSCORE_AGENT_ID="GOUSTO TESTS")



execution_vars = {
    "PSCORE_ENVIRONMENT": RUN_LOCAL,
    "PSCORE_BROWSER": CHROME,
    "PSCORE_BROWSER_VERSION": "",
    "PSCORE_HOMEPAGE": GOUSTO_HEALTHY_RECIPE_PAGE,
    "PSCORE_ANDROID_CHROME_PACKAGE_NAME": 'com.chrome.beta'
}


current_environment = get_environment_variable("TEAMCITY_STAGE")
message = "Setting variables for {}".format(current_environment)


set_environment_variables(execution_vars)

if current_environment is None:
    # assume not on teamcity, thus local dev machine
    set_environment_variables(user_local_settings)