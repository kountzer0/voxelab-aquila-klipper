# Adding a CR Touch to the Aquila FFP0173 v1.0.1

The dedicated 5-pin BL-Touch header on the FFP0173 v1.0.1 board uses PB0 for control and PB1 for the probe signal. This mapping is documented in the [FFP0173 v1.0.1 board pinout](https://gist.github.com/SteveGotthardt/f89cc4a40f81650fd708a5cfce5a42e3).

In `[stepper_z]`, replace the mechanical Z endstop line with:

```ini
endstop_pin: probe:z_virtual_endstop
```

Remove `position_endstop` from `[stepper_z]`, then add and calibrate a probe section:

```ini
[bltouch]
sensor_pin: ^PB1
control_pin: PB0
x_offset: 0.0  # measure nozzle-to-probe offset for your mount
y_offset: 0.0  # measure nozzle-to-probe offset for your mount
z_offset: 0.0  # placeholder; calibrate with PROBE_CALIBRATE

[safe_z_home]
home_xy_position: 117.5, 117.5  # adjust so the probe is over bed center
speed: 50
z_hop: 10
z_hop_speed: 5
```

`home_xy_position` is a nozzle position. Calculate it from your bed center and measured probe offsets so the probe itself lands over the bed. Set actual mesh limits for the installed carriage and bed. Do not print with the placeholder Z offset.

Follow [Klipper's BL-Touch setup and calibration steps](https://www.klipper3d.org/BLTouch.html) before enabling probe homing or bed mesh.
