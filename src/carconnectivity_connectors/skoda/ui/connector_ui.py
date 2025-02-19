""" User interface for the Skoda connector in the Car Connectivity application. """
from __future__ import annotations
from typing import TYPE_CHECKING

import os

import flask

from carconnectivity_connectors.base.ui.connector_ui import BaseConnectorUI

if TYPE_CHECKING:
    from typing import Optional, List, Dict, Union, Literal

    from carconnectivity_connectors.base.connector import BaseConnector


class ConnectorUI(BaseConnectorUI):
    """
    A user interface class for the Skoda connector in the Car Connectivity application.
    """
    def __init__(self, connector: BaseConnector):
        blueprint: Optional[flask.Blueprint] = flask.Blueprint(name='skoda', import_name='carconnectivity-connector-skoda', url_prefix='/skoda',
                                                                    template_folder=os.path.dirname(__file__) + '/templates')
        super().__init__(connector, blueprint=blueprint)

    def get_nav_items(self) -> List[Dict[Literal['text', 'url', 'sublinks', 'divider'], Union[str, List]]]:
        """
        Generates a list of navigation items for the Skoda connector UI.
        """
        return super().get_nav_items()

    def get_title(self) -> str:
        """
        Returns the title of the connector.

        Returns:
            str: The title of the connector, which is "Skoda".
        """
        return "Skoda"
