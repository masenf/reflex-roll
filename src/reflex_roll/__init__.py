"""A more fun connection down indicator your App users will love."""

import sys
from base64 import b64encode
from importlib.resources import files
from pathlib import Path

ROLL_LOADING_INDICATOR = "rollLoadingIndicator"
ROLL_FILE_NAME = "ezgif-7-4353d96d35.gif"

try:
    import reflex.components.core.banner as banner
    from reflex.vars import Var
    from reflex.utils.imports import ImportVar

    class RollPulser(banner.WifiOffPulse):
        def _get_imports(self):
            return {
                **super()._get_imports(),
                "../utils/roll.js": [ImportVar(tag=ROLL_LOADING_INDICATOR)],
            }

        def _render(self):
            self.children = []
            tag = super()._render()
            tag.name = "img"
            tag.add_props(
                src=Var.create_safe(
                    ROLL_LOADING_INDICATOR, _var_is_local=False, _var_is_string=False
                )
            )
            tag.remove_props("size")
            return tag

    web_utils = Path(".web", "utils")
    if web_utils.is_dir():
        roll_js = web_utils / "roll.js"
        if not roll_js.exists():
            roll = (
                "data:image/gif;base64,"
                + b64encode((files(__name__) / ROLL_FILE_NAME).read_bytes()).decode()
            )
            (web_utils / "roll.js").write_text(
                f"export const {ROLL_LOADING_INDICATOR} = '{roll}';"
            )
        banner.WifiOffPulse = RollPulser
except ImportError:
    if __name__ in sys.modules:
        try:
            del sys.modules[__name__]
        except KeyError:
            pass
