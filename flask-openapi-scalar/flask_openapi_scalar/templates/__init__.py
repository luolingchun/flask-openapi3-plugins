# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2024/4/23 14:46
scalar_html_string = """
<!doctype html>
<html>
    <head>
        <title>Scalar API</title>
        <meta charset="utf-8" />
        <meta
        name="viewport"
        content="width=device-width, initial-scale=1" />
        <link rel="shortcut icon" href="scalar/images/scalar.svg">
    </head>
    <body>
        <script
        id="api-reference"
        data-url="{{ doc_url }}">
        </script>
        <script>
        const scalar_config = JSON.parse(`{{ scalar_config|default('{}')|tojson }}`);
        var configuration = {...scalar_config};
        var apiReference = document.getElementById('api-reference');
        apiReference.dataset.configuration = JSON.stringify(configuration);
        </script>
        <script src="scalar/js/scalar.standalone.js"></script>
    </body>
</html>
"""
