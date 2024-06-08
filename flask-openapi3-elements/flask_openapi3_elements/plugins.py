import os

from flask import Blueprint, render_template_string, current_app
from flask_openapi3.plugins import BasePlugin

from .templates import elements_html_string


class RegisterPlugin(BasePlugin):
    name = "elements"
    display_name = "Elements"

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
                current_app.config.get("ELEMENTS_HTML_STRING") or elements_html_string,
                doc_url=doc_url,
                elements_config=current_app.config.get("ELEMENTS_CONFIG")
            )
        )

        return blueprint
