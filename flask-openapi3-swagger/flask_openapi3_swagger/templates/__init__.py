# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2024/4/23 14:46
swagger_html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Swagger UI</title>
    <link rel="shortcut icon" href="swagger/images/swagger.svg">
    <link rel="stylesheet" type="text/css" href="swagger/css/swagger-ui.css">
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }

        *, *:before, *:after {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            background: #fafafa;
        }
    </style>
</head>
<body>
<div id="swagger-ui"></div>
<script src="swagger/js/swagger-ui-bundle.js"></script>
<script src="swagger/js/swagger-ui-standalone-preset.js"></script>
<script>
    const swagger_config = JSON.parse(`{{ swagger_config|default('{}')|tojson }}`);
    url = new URL("{{doc_url}}", window.location.href).href;
    window.onload = function () {
        // Begin Swagger UI call region
        window.ui = SwaggerUIBundle({
        ...{
            url: url,
            dom_id: "#swagger-ui",
            deepLinking: true,
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIStandalonePreset
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout",
            showExtensions: true,
            showCommonExtensions: true
        },
        ...swagger_config
        })
        // End Swagger UI call region
        const oauthConfig = {{ oauth_config|tojson }};
        if (oauthConfig != null) {
            window.ui.initOAuth({
                clientId: oauthConfig.clientId,
                clientSecret: oauthConfig.clientSecret,
                realm: oauthConfig.realm,
                appName: oauthConfig.appName,
                scopeSeparator: oauthConfig.scopeSeparator,
                scopes: oauthConfig.scopes,
                additionalQueryStringParams: oauthConfig.additionalQueryStringParams,
                usePkceWithAuthorizationCodeGrant: oauthConfig.usePkceWithAuthorizationCodeGrant
            })
        }
    }
</script>
</body>
</html>
"""
swagger_oauth2_redirect_html_string = """
<!doctype html>
<html lang="en-US">
<head>
    <title>Swagger UI: OAuth2 Redirect</title>
</head>
<body>
<script>
    'use strict';
    function run () {
        var oauth2 = window.opener.swaggerUIRedirectOauth2;
        var sentState = oauth2.state;
        var redirectUrl = oauth2.redirectUrl;
        var isValid, qp, arr;

        if (/code|token|error/.test(window.location.hash)) {
            qp = window.location.hash.substring(1).replace('?', '&');
        } else {
            qp = location.search.substring(1);
        }

        arr = qp.split("&");
        arr.forEach(function (v,i,_arr) { _arr[i] = '"' + v.replace('=', '":"') + '"';});
        qp = qp ? JSON.parse('{' + arr.join() + '}',
                function (key, value) {
                    return key === "" ? value : decodeURIComponent(value);
                }
        ) : {};

        isValid = qp.state === sentState;

        if ((
          oauth2.auth.schema.get("flow") === "accessCode" ||
          oauth2.auth.schema.get("flow") === "authorizationCode" ||
          oauth2.auth.schema.get("flow") === "authorization_code"
        ) && !oauth2.auth.code) {
            if (!isValid) {
                oauth2.errCb({
                    authId: oauth2.auth.name,
                    source: "auth",
                    level: "warning",
                    message: "Authorization may be unsafe, passed state was changed in server. The passed state wasn't returned from auth server."
                });
            }

            if (qp.code) {
                delete oauth2.state;
                oauth2.auth.code = qp.code;
                oauth2.callback({auth: oauth2.auth, redirectUrl: redirectUrl});
            } else {
                let oauthErrorMsg;
                if (qp.error) {
                    oauthErrorMsg = "["+qp.error+"]: " +
                        (qp.error_description ? qp.error_description+ ". " : "no accessCode received from the server. ") +
                        (qp.error_uri ? "More info: "+qp.error_uri : "");
                }

                oauth2.errCb({
                    authId: oauth2.auth.name,
                    source: "auth",
                    level: "error",
                    message: oauthErrorMsg || "[Authorization failed]: no accessCode received from the server."
                });
            }
        } else {
            oauth2.callback({auth: oauth2.auth, token: qp, isValid: isValid, redirectUrl: redirectUrl});
        }
        window.close();
    }

    if (document.readyState !== 'loading') {
        run();
    } else {
        document.addEventListener('DOMContentLoaded', function () {
            run();
        });
    }
</script>
</body>
</html>
"""
