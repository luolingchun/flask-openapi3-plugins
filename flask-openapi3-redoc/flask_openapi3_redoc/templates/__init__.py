redoc_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>ReDoc</title>
    <link rel="shortcut icon" href="static/images/redoc.svg">
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--link href="static/css/google-fonts.css" rel="stylesheet" -->
    <!-- ReDoc doesn't change outer page styles -->
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
<redoc spec-url='{{ doc_url }}'></redoc>
<script src="static/js/redoc.standalone.js"></script>
</body>
</html>
"""