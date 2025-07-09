# Honeywell Hot Water Controller for Home Assistant

## THIS IS NOT IMPLEMENTED!!!!!  DO NOT USE. See [rpi_EnviraCOM](https://github.com/latetedemelon/rpi_EnviraCOM)


![beta_badge](https://img.shields.io/badge/maturity-Beta-yellow.png)
![release_badge](https://img.shields.io/github/v/release/rsnodgrass/hass-honeywell-whc.svg)
![release_date](https://img.shields.io/github/release-date/rsnodgrass/hass-honeywell-whc.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=WREP29UDAMB6G)

Home Assistant support for [Honeywell (Resideo) digital hot water controllers](https://github.com/rsnodgrass/pyhoneywell_whc) used on Bradford White, AO Smith, Rheem and other hot water tanks.

## Support

Visit the Home Assistant community if you need [help with installation and configuration]().

### Supported Features

- water temperature (&deg;F) for upper and lower tank
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
water_heater:
  - platform: honeywell_whc
    name: "Hot Water Tank"
    port: /dev/ttyUSB0
```

### Step 3: Add Lovelace Card

The following is a simplest Lovelace card which shows data from the Flo sensors:

```yaml
type: entities
entities:
  - entity: water_heater.honeywell_whc
  - entity: sensor.honeywell_whc_temp_upper
  - entity: sensor.honeywell_whc_temp_lower
```

## See Also

* [pyhoneywell_whc](https://github.com/rsnodgrass/pyhoneywell_whc)

## Automation Ideas

- home/away/vacation mode
- setback schedule
- operation_mode: eco (forced 120?)


# Bradford White/Honeywell WiFi Control

Bradford White sold several "ICON" kits that allowed controlling the Honeywell gas valve temperature settings through a remote thermostat with scheduling, as well as water leak detection and automatic water shutoffs. These worked with earlier WV8840 and WV8860 models with a Accessory Module Kit which translated the older serial communication from the front mounted COM port to the EnviraCOM 1.1 protocol. This Accessory Model allowed hooking up their ICON EnviraCOM smart Setback Controller (PN 239-48559-00) thermostat which enabled setting the maximum hot water temperature, as well as a full weeks schedule for hot water tank temps at multiple times of the day. The ICON Setback Controller was a EnviraCOM compatible thermostat controller which meant that other EnviraCON heater controls might work as well. Interestingly enough, the Rheem EcoNet Home Comfort WiFi Module speaks EnviraCOM as well, and completely works with the ICON Accessory Module Kit to control the Honeywell temperature settings.  Not only that, but the Rheem EcoNet unit also includes WiFi ability (allowing control via iOS and Android apps), but also includes a water leak sensor, and can be purchased for about $20 on eBay. This also means that any gas water heater with the WV8840/WV8860 model controls can be integrated easily into home automation systems that support EcoNet.

Parts needed:

* Bradford White ICON 239-47872-00 Accessory Module Kit (part WHACCPKG1005) or the individual module (part WHAM03A1004)

* Rheem EcoNet Home Comfort WiFi Module for **Gas Heaters** (part REWRA631GWH / PCB board RCBD-0012042428-00-C)

### Wiring Rheem EcoNet to ICON Accessory Module

| Accessory Module Wire | Rheem EcoNet Wire | EnviraCOM Pin | Description |
| --------------------- | ----------------- | ------------- | ----------- |
| D/1                   | Yellow            | 1             | Data/Signal |
| R/2                   | Black             | 2             | 24 Vac      |
| C/3                   | Red               | 3             | 24 Vac      |

Connect the above wires from the Rheem EcoNet WiFi Module to the listed connection on the ICON Acessory Module. Then follow the standard Rheem EcoNet settings to connect to WiFi, and you can then control any gas water heater with these Honeywell smart gas valves.  Besides the iOS/Android apps, you can also now easily integrate this with your favorite smart home automation platform, such as Home Assistant.  The only thing that does't appear to work is that the Home/Away setting does not seem to change any behavior for the water heater.

### Honeywell Red Dial Temperature Settings

Regarding the dial on the front of the Honeywell WV8840/WV8860.

| Dial Setting | Min Temp (F) | Max Temp (F) |
| ------------ | ------------ | ------------ |
| LOW          | 55           | 55           |
| (dot)        |              | 85           |
| HOT          |              | 125          |
| A            | 90           | 125          |
| B            | 90           | 140          |
| C            | 90?          | 140?         |
| VERY HOT     | 90?          | 140?         |


* https://www.raspberrypi.org/forums/viewtopic.php?t=136314 ***
