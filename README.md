# ConfigIt

Configuration manager for Linux users who has more then one computer in use. The idea is to store your configuratoin files in private Github repository as simple directory structures called 'profiles'.

## Configuration

Configuration file name: `~/.config/configit/configit.ini`

```
[profile]
name = default

[github]
token = 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
repo = configit-files

[default]
etc = etc.list
local = local.list
```

Create `etc.list` and `local.list` in `~/.config/configit` directory. List files must contain only one absolute path to configuration file per line:

```
/etc/vimrc
/etc/example.conf
```

You can define more list files using `example = filename` key-values to separate your configuration files as you wish. Just be sure you have created the list file in the `~/.config/configit` configuration directory.

Or you can create and download remote configuration files.

