from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests
import json
from requests.structures import CaseInsensitiveDict


#class GreetingsInput(BaseModel):
#    greetings: str = Field(..., description="Greeting message to be sent")


class OdooTool(BaseTool):
    """
    Get active products
    """
    name: str = "Get active products"
    #args_schema: Type[BaseModel] = GreetingsInput
    description: str = "Get active products from Odoo"

    def _execute(self):

        url = self.get_tool_config("ODOO_URL") + "/get_products"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = self.get_tool_config("API_Key")
        headers["AWS-API-Secret"] = self.get_tool_config("API_SECRET_TOKEN")
        headers["Content-Type"] = ""
        resp = requests.get(url, headers=headers)
        return resp.json()
