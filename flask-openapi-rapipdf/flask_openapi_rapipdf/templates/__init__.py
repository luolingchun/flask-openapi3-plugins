rapipdf_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1,user-scalable=yes">
    <title>RapiPDF</title>
    <link rel="shortcut icon" href="rapipdf/images/rapipdf.svg">
    <script src="rapipdf/js/rapipdf-min.js"></script>
</head>
<body>
<rapi-pdf spec-url = '{{ doc_url}}'></rapi-pdf>
<script>
    const rapipdf_config = JSON.parse(`{{ rapipdf_config|default('{}')|tojson }}`);
    var rapiPdf = document.querySelector("rapi-pdf");
    var specUrl = new URL("{{ doc_url }}", window.location.href).href;
    rapiPdf.setAttribute("spec-url", specUrl);
    for(var k in rapipdf_config) {
        rapiPdf.setAttribute(k, rapipdf_config[k]);
    }
</script>
</body>
</html>
"""
