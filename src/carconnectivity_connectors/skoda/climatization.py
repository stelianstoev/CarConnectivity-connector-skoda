"""
Module for charging for skoda vehicles.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from carconnectivity.climatization import Climatization
from carconnectivity.objects import GenericObject
from carconnectivity.vehicle import ElectricVehicle

from carconnectivity_connectors.skoda.error import Error

if TYPE_CHECKING:
    from typing import Optional, Dict


class SkodaClimatization(Climatization):  # pylint: disable=too-many-instance-attributes
    """
    SkodaClimatization class for handling Skoda vehicle climatization information.

    This class extends the Climatization class and includes an enumeration of various
    charging states specific to Skoda vehicles.
    """
    def __init__(self, vehicle: ElectricVehicle | None = None, origin: Optional[Climatization] = None) -> None:
        if origin is not None:
            super().__init__(origin=origin)
            self.settings: Climatization.Settings = SkodaClimatization.Settings(origin=origin.settings)
        else:
            super().__init__(vehicle=vehicle)
            self.settings: Climatization.Settings = SkodaClimatization.Settings(origin=self.settings)
        self.errors: Dict[str, Error] = {}

    class Settings(Climatization.Settings):
        """
        This class represents the settings for a skoda car climatiation.
        """
        def __init__(self, parent: Optional[GenericObject] = None, origin: Optional[Climatization.Settings] = None) -> None:
            if origin is not None:
                super().__init__(origin=origin)
            else:
                super().__init__(parent=parent)
