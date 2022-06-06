# The config.toml file

Configuration file for RRPM

`config.toml` is the file used to configure settings for RRPM. It is located in `%LOCALAPPDATA%\rrpm` on Windows and `~/.config/rrpm` on Unix.

## [root] Section

- `dir`: String that determines the location of where to store projects.
- `ext_dir`: String that determines the location of where to look for extensions.

## [cli] Section

- `display_output`: Boolean that determines if the raw output of the commands ran or shown or not.
- `extensions`: List of strings where each determines the file name of an extension.
