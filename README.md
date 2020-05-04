# Docker Plugin API in Python

This module contains some abstractions to simplify creation
of own plugins for Docker Engine.

It currently contains entities for:

- Plugin,
- IpamDriver,
- NetworkDriver.

## Examples

Check out following real-life plugins that utilize this package:

| Plugin | Type | URL |
| ------ | ---- | --- |
| jacekkow/pyipam | IpamDriver | https://github.com/jacekkow/docker-plugin-pyipam |
| jacekkow/pyveth | NetworkDriver | https://github.com/jacekkow/docker-plugin-pyveth |
