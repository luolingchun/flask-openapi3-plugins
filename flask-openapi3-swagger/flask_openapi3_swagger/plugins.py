# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2024/4/22 16:13
import os

from flask import Blueprint, render_template_string, current_app
from flask_openapi3.plugins import BasePlugin

from .templates import swagger_html_string, swagger_oauth2_redirect_html_string


class RegisterPlugin(BasePlugin):
    name = "swagger"
    display_name = "Swagger"

    @classmethod
    def register(cls, doc_url: str) -> Blueprint:
        _here = os.path.dirname(__file__)
        template_folder = os.path.join(_here, "templates")
        static_folder = os.path.join(template_folder, cls.name)
        blueprint = Blueprint(
            cls.name,
            __name__,
            template_folder=template_folder,
            static_folder=static_folder
        )

        blueprint.add_url_rule(
            rule=f"/{cls.name}",
            endpoint=cls.name,
            view_func=lambda: render_template_string(
                current_app.config.get("SWAGGER_HTML_STRING") or swagger_html_string,
                doc_url=doc_url,
                swagger_config=current_app.config.get("SWAGGER_CONFIG"),
                oauth_config=current_app.config.get("OAUTH_CONFIG")
            )
        )
        blueprint.add_url_rule(
            rule=f"/oauth2-redirect.html",
            endpoint="oauth2-redirect",
            view_func=lambda: render_template_string(
                swagger_oauth2_redirect_html_string
            )
        )
        return blueprint
