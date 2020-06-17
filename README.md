# Honeywell (Resideo) Hot Water Controller for Home Assistant

![beta_badge](https://img.shields.io/badge/maturity-Beta-yellow.png)
![release_badge](https://img.shields.io/github/v/release/rsnodgrass/hass-honeywell-whc.svg)
![release_date](https://img.shields.io/github/release-date/rsnodgrass/hass-honeywell-whc.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=WREP29UDAMB6G)

Home Assistant support for [Honeywell (Resideo) hot water controllers](https://github.com/rsnodgrass/pyhoneywell_whc) used on Bradford White, AO Smith, Rheem and other hot water tanks.

## Support

Visit the Home Assistant community if you need [help with installation and configuration]().

### Supported Features

- sensors: water temperature (&deg;F) for upper and lowe tank
- heater running on/off detection

#### Not Supported

- setting target temperature
- home/away/vacation modes

## Installation

#### Versions

The 'master' branch of this custom component is considered unstable, alpha quality and not guaranteed to work.
Please make sure to use one of the official release branches when installing using HACS, see [what has changed in each version](https://github.com/rsnodgrass/hass-flo-water/releases).

### Step 1: Install Custom Component

Make sure that [Home Assistant Community Store (HACS)](https://github.com/custom-components/hacs) is setup, then add the "Integration" repository: rsnodgrass/hass-honeywell-whc.

Note: Manual installation by direct download and copying is not supported, if you have issues, please first try installing this integration with HACS.

### Step 2: Configure Sensors

Example configuration:

```yaml
[water_heater](https://www.home-assistant.io/integrations/water_heater/):
  - platform: honeywell_whc
    port: /dev/ttyUSB0
```

### Step 3: Add Lovelace Card

The following is a simplest Lovelace card which shows data from the Flo sensors:

```yaml
type: entities
entities:
  - entity: water_heater.honeywell
  - entity: sensor.honeywell_water_heater_temp_upper
  - entity: sensor.honeywell_water_heater_temp_lower
```

## See Also

* [pyhoneywell_whc](https://github.com/rsnodgrass/pyhoneywell_whc)

## Automation Ideas

- home/away/vacation mode
- setback schedule
- operation_mode: eco
