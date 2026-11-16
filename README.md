# Klipper configuration for the Voxelab Aquila

Reusable stock profile for the Voxelab Aquila FFP0173 v1.0.1 mainboard. The motion, heater, fan, and endstop pins follow Klipper's Aquila example configuration. This repository keeps machine-specific tuning and CR Touch offsets out of the default profile.

## Before use

- Confirm the board revision and MCU marking. The MCU firmware target differs between N32G452, STM32/GD32, and HC32 boards even when the mainboard pin map is similar. This profile does not include a prebuilt firmware binary.
- Set `[mcu] serial` in `printer.cfg` to the actual path from `ls /dev/serial/by-id/`.
- Confirm X/Y/Z motion and endstop operation before printing. Calibrate the extruder, heaters, and Z reference for your machine.
- This profile uses the mechanical Z endstop by default. See `docs/crtouch.md` to add a CR Touch.
- `[include mainsail.cfg]` assumes Mainsail's `mainsail.cfg` is installed in the config directory. Remove that include and the related virtual-SD/Mainsail sections if using another frontend.

## CR Touch

The optional CR Touch guide is for the dedicated BL-Touch 5-pin header on the FFP0173 v1.0.1 board. Its control and sensor signals map to PB0 and PB1. Probe XY/Z offsets and mesh limits must be calibrated for the installed mount and bed.

## Firmware target

For N32G452 users, `firmware/configure_n32g452.py` and `firmware/klipper-n32g452.config` document the N32G452 Klipper build used with the FFP0173 board: 28 KiB bootloader, 8 MHz reference, USART1 PA9/PA10. Build from your own Klipper checkout and follow the flashing procedure for your board variant.

For the G32/STM32 Aquila configuration, see [aquila-x2-g32-klipper](https://github.com/kountzer0/aquila-x2-g32-klipper).

## Upstream

The base pin map follows [Klipper's Voxelab Aquila example](https://github.com/Klipper3d/klipper/blob/master/config/printer-voxelab-aquila-2021.cfg).

## License

GPL-3.0-or-later.
