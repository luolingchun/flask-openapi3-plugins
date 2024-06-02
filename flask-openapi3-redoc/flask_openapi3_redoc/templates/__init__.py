redoc_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>ReDoc</title>
    <link rel="shortcut icon" href="redoc/images/redoc.svg">
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
  <div id="redoc"></div>
  <script src="redoc/js/redoc.standalone.js"></script>
  <script>
    const redoc_config = JSON.parse(`{{ redoc_config|default('{}')|tojson }}`);
    Redoc.init(
      "{{ doc_url }}", redoc_config,
      document.getElementById("redoc"))
  </script>
</body>
</html>
"""
