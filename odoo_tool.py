from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests
import json
from requests.structures import CaseInsensitiveDict


class OdooToolInput(BaseModel):
   pass


class OdooTool(BaseTool):
    """
    Get active products from Odoo
    """
    name: str = "Get active products from Odoo"
    args_schema: Type[BaseModel] = OdooToolInput
    description: str = "Get active products from Odoo"

    def _execute(self):

        url = self.get_tool_config("ODOO_URL") + "/get_products"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic " + self.get_tool_config("API_Key")
        headers["AWS-API-Secret"] = self.get_tool_config("API_SECRET_TOKEN")
        headers["Content-Type"] = ""
        resp = requests.get(url, headers=headers)
        return resp.json()
