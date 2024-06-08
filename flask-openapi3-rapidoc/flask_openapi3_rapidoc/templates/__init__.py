rapidoc_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1,user-scalable=yes">
    <title>RapiDoc</title>
    <link rel="shortcut icon" href="rapidoc/images/rapidoc.svg">
</head>
<body>
<rapi-doc spec-url='{{ doc_url }}'></rapi-doc>
<script>
    const rapidoc_config = JSON.parse(`{{ rapidoc_config|default('{}')|tojson }}`);
    var rapiDoc = document.querySelector("rapi-doc");
    var specUrl = new URL("{{ doc_url }}", window.location.href).href;
    rapiDoc.setAttribute("spec-url", specUrl);
    for(var k in rapidoc_config) {
        rapiDoc.setAttribute(k, rapidoc_config[k]);
    }
</script>
<script src="rapidoc/js/rapidoc-min.js"></script>
</body>
</html>
"""
