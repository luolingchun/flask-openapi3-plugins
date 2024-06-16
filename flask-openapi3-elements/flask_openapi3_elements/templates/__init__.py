elements_html_string = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Elements</title>
    <link rel="shortcut icon" href="elements/images/elements.svg">
    <script src="elements/js/web-components.min.js"></script>
    <link rel="stylesheet" href="elements/css/styles.min.css">
</head>
<body>
<elements-api
    apiDescriptionUrl="{{ doc_url }}"
    router="hash"
/>
<script>
    const elements_config = JSON.parse(`{{ elements_config|default('{}')|tojson }}`);
    var elementsDoc = document.querySelector("elements-api");
    var specUrl = new URL("{{ doc_url }}", window.location.href).href;
    elementsDoc.setAttribute("apiDescriptionUrl", specUrl);
    for(var k in elements_config) {
        elementsDoc.setAttribute(k, elements_config[k]);
    }
</script>
</body>
</html>
"""
