"""
Honeywell Water Heater Controller for Home Assistant
See https://github.com/rsnodgrass/hass-honeywell-whc
"""
import logging
import voluptuous as vol

from homeassistant.components.water_heater import (
    PLATFORM_SCHEMA,
    STATE_ECO,
    STATE_ELECTRIC,
    STATE_GAS,
    STATE_HEAT_PUMP,
    STATE_HIGH_DEMAND,
    STATE_OFF,
    STATE_PERFORMANCE,
    SUPPORT_OPERATION_MODE,
    SUPPORT_TARGET_TEMPERATURE,
    WaterHeaterEntity,
)
from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_TEMPERATURE,
    CONF_PORT,
    TEMP_FAHRENHEIT,
)
import homeassistant.helpers.config_validation as cv

from pyhoneywell_whc import PyHoneywellWaterHeaterControl

LOG = logging.getLogger(__name__)

DOMAIN = 'honeywell_whc'
HONEYWELL_DATA = "honeywell_whc"

NOTIFICATION_ID = 'honeywell_whc_notification'

CONF_AUTO_DISCOVER = 'discovery'
CONF_LOCATION_ID = 'location_id'
CONF_STARTDATE = 'startdate'

SUPPORTED_FLAGS_HEATER = SUPPORT_TARGET_TEMPERATURE | SUPPORT_OPERATION_MODE

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_PORT): cv.string
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Honeywell Water Heater Control Control System"""

    conf = config[FLO_DOMAIN]

    hass.data[HONEYWELL_DATA]["water_heaters"] = []
    
    tty = config[CONF_PORT]
    water_heater = PyHoneywellWaterHeaterController(tty)

    hass_water_heaters = [ HoneywellWaterHeater(water_heater) ]
    add_entities(hass_water_heaters)
    hass.data[ECONET_DATA]["water_heaters"].extend(hass_water_heaters)


    def service_handle(service):
        """Handle the service calls."""
        entity_ids = service.data.get("entity_id")
        all_heaters = hass.data[HONEYWELL_DATA]["water_heaters"]
        _heaters = [
            x for x in all_heaters if not entity_ids or x.entity_id in entity_ids
        ]

 #       for _water_heater in _heaters:
 #           if service.service == SERVICE_DELETE_VACATION:
 #               for vacation in _water_heater.water_heater.vacations:
 #                   vacation.delete()
 #
 #           _water_heater.schedule_update_ha_state(True)

#    hass.services.register(
#        DOMAIN, SERVICE_ADD_VACATION, service_handle, schema=ADD_VACATION_SCHEMA
#    )
 
    return True

class HoneywelllWaterHeater(Entity):
    """Base Entity class for Honeywell water heater controller"""

    def __init__(self, hass, water_heater):
        """Initialize the water heater."""
        self._hass = hass
        self.water_heater = water_heater
        self.supported_modes = [ 'electric_only' ]

    @property
    def name(self):
        """Return the device name."""
        return self.water_heater.name

    @property
    def available(self):
        """Return if the the device is online or not."""
        return self.water_heater.is_connected

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_FAHRENHEIT

    @property
    def extra_state_attributes(self):
        """Return the optional device state attributes."""
        data = {}
        return data
    
    @property
    def current_operation(self):
        """
        Return current operation as one of the following.
           ["eco", "heat_pump", "high_demand", "electric_only"]
        """
        return "electric_only"

    @property
    def operation_list(self):
        """List of available operation modes."""
        op_list = []
        for mode in self.supported_modes:
            ha_mode = self.econet_state_to_ha.get(mode)
            if ha_mode is not None:
                op_list.append(ha_mode)
        return op_list

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORTED_FLAGS_HEATER


    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        target_temp = kwargs.get(ATTR_TEMPERATURE)
        if target_temp is not None:
            # self.water_heater.set_target_set_point(target_temp)
        else:
            _LOGGER.error("A target temperature must be provided")

    def set_operation_mode(self, operation_mode):
        """Set operation mode."""
        op_mode_to_set = self.ha_state_to_econet.get(operation_mode)
        if op_mode_to_set is not None:
            # self.water_heater.set_mode(op_mode_to_set)
        else:
            _LOGGER.error("An operation mode must be provided")

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self.water_heater.target_temp
