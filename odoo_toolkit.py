from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from odoo_tool import OdooTool


class OdooToolkit(BaseToolkit, ABC):
    name: str = "Odoo Toolkit"
    description: str = "Odoo Tool kit contains all tools related to Odoo"

    def get_tools(self) -> List[BaseTool]:
        return [OdooTool()]

    def get_env_keys(self) -> List[str]:
        return ["ODOO_URL", "API_SECRET_TOKEN", "API_Key"]