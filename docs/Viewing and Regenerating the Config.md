# Viewing and Regenerating the Config

Corrupted the config file? Regenerate it using the rrpm config --regenerate command

## Viewing the Current Config File

The current config file can be viewed by running the command `rrpm config`.

```bash
$ python -m rrpm config
{
    'root': {'dir': '%USERPROFILE%\\Projects', 'ext_dir': '%LOCALAPPDATA%\\rrpm\\extensions'},
    'cli': {'display_output': False, 'extensions': ['myext']}
}
```

### Regenerating the Config File

```bash
$ python -m rrpm config --regenerate
Config file regenerated successfully!
```

