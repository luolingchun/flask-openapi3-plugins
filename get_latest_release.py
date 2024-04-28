# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2024/4/21 14:54
import os
import re
import sys

import requests

here = os.path.dirname(__file__)
cdn_base_url = "https://cdn.jsdelivr.net/npm"


def get_old_version(version_file):
    with open(version_file, "r", encoding="utf-8") as f:
        content = f.read()
        old_version = re.findall(r"__version__ = \"(.*?)\"", content)[0]

    return old_version


def download_swagger(latest_version):
    version_file = os.path.join(here, "flask-openapi3-swagger", "__version__.py")
    old_version = get_old_version(version_file)

    is_update = False
    if latest_version != old_version:
        # download swagger-ui-bundle.js
        response = requests.get(f"{cdn_base_url}/swagger-ui-dist@{latest_version}/swagger-ui-bundle.js")
        bundle_js = os.path.join(here, "flask-openapi3-swagger", "js", "swagger-ui-bundle.js")
        if response.status_code == 200:
            with open(bundle_js, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Succeed to download swagger-ui-bundle.js. version: {latest_version}")
        else:
            raise Exception(f"Failed to download swagger-ui-bundle.js. version: {latest_version}")
        # download swagger-ui-standalone-preset.js
        response = requests.get(f"{cdn_base_url}/swagger-ui-dist@{latest_version}/swagger-ui-standalone-preset.js")
        standalone_preset_js = os.path.join(here, "flask-openapi3-swagger", "js", "swagger-ui-standalone-preset.js")
        if response.status_code == 200:
            with open(standalone_preset_js, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Succeed to download swagger-ui-standalone-preset.js. version: {latest_version}")
        else:
            raise Exception(f"Failed to download swagger-ui-standalone-preset.js. version: {latest_version}")
        # download swagger-ui.css
        response = requests.get(f"{cdn_base_url}/swagger-ui-dist@{latest_version}/swagger-ui.css")
        swagger_ui_css = os.path.join(here, "flask-openapi3-swagger", "css", "swagger-ui.css")
        if response.status_code == 200:
            with open(swagger_ui_css, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Succeed to download swagger-ui.css. version: {latest_version}")
        else:
            raise Exception(f"Failed to download swagger-ui.css. version: {latest_version}")

        # update version
        with open(version_file, "w", encoding="utf-8") as f:
            f.write(f"""# -*- coding: utf-8 -*-\n\n__version__ = "{latest_version}"\n""")

        is_update = True
    return is_update


def get_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latest_version = data["tag_name"].lstrip('v')
        print(f"The latest release of {owner}/{repo} is: {latest_version}")
    else:
        raise Exception(f"Failed to retrieve latest release for {owner}/{repo}")

    is_update = False
    if repo == "swagger-ui":
        is_update = download_swagger(latest_version)

    if is_update:
        print(f"::set-output name=version::{latest_version}")
        sys.exit(0)
    else:
        sys.exit(1)


def main():
    argv = sys.argv
    owner, repo = argv[0], argv[1]
    get_latest_release(owner, repo)


if __name__ == "__main__":
    main()
