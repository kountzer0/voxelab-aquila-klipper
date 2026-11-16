#!/usr/bin/env python3
"""Write the confirmed Voxelab Aquila N32G452 Klipper build config."""

from pathlib import Path
import os
import sys

repo = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(repo / "lib" / "kconfiglib"))
import kconfiglib

os.chdir(repo)
kconf = kconfiglib.Kconfig("src/Kconfig")

for symbol in (
    "LOW_LEVEL_OPTIONS",
    "MACH_STM32",
    "MACH_N32G452",
    "STM32_FLASH_START_7000",
    "STM32_CLOCK_REF_8M",
    "STM32_SERIAL_USART1",
):
    item = kconf.syms.get(symbol)
    if item is None:
        raise SystemExit(f"Klipper source lacks required option: {symbol}")
    item.set_value(2)

kconf.write_config(".config")
for symbol in (
    "MACH_STM32",
    "MACH_N32G452",
    "STM32_FLASH_START_7000",
    "STM32_CLOCK_REF_8M",
    "STM32_SERIAL_USART1",
    "MCU",
    "CLOCK_FREQ",
    "FLASH_APPLICATION_ADDRESS",
):
    item = kconf.syms[symbol]
    print(f"{symbol}={item.str_value}")
