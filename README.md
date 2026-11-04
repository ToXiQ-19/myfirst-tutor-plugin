# My First Tutor Plugin

A custom [Tutor](https://docs.tutor.edly.io/) plugin for managing Open edX theme branding.

The plugin provides a command-line interface to switch between Indigo and Pink themes by updating Tutor configuration, rebuilding the required images, and restarting the local Open edX environment.

## Features

- Switch between Indigo and Pink themes.
- List available themes and their primary colors.
- Update Indigo primary color configuration.
- Build Open edX and MFE Docker images.
- Restart the local Tutor environment.
- Extend Tutor through its plugin and hook system.

## Supported Themes

| Theme | Primary Color | Hex Code |
|---|---|---|
| Indigo | Indigo Blue | `#15376D` |
| Pink | Pink | `#E91E63` |

## Requirements

- Python 3.9+
- Tutor 19.x
- Docker
- A working local Open edX installation
- Tutor Indigo plugin
- Tutor MFE plugin

## Installation

Clone the repository:

```bash
git clone https://github.com/ToXiQ-19/myfirst-tutor-plugin.git
cd myfirst-tutor-plugin
```

Install the plugin:

```bash
pip install -e .
```

Enable it:

```bash
tutor plugins enable myfirstplugin
```

## Usage

List available themes:

```bash
tutor themes list
```

Switch to Pink:

```bash
tutor themes set pink
```

Switch to Indigo:

```bash
tutor themes set indigo
```

Theme switching updates the Indigo primary color, builds the Open edX and MFE images, and restarts the local Tutor environment.

Image builds may take several minutes.

## Theme Assets

The repository includes custom LMS Sass styling:

```text
themes/
└── custom/
    └── lms/
        └── static/
            └── sass/
                └── _extras.scss
```

## Project Structure

```text
myfirst-tutor-plugin/
├── myfirstplugin/
│   ├── __init__.py
│   ├── plugin.py
│   └── theme_manager.py
├── themes/
│   └── custom/
│       └── lms/
│           └── static/
│               └── sass/
│                   └── _extras.scss
├── tests/
├── docs/
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

## Configuration

| Variable | Default |
|---|---|
| `MYFIRSTPLUGIN_DEFAULT_THEME` | `indigo` |

The available theme colors are currently defined in the theme manager.

## Compatibility

The current implementation targets Tutor 19.x.

Compatibility with other Tutor versions has not yet been verified.

## Development

Contributions and suggestions are welcome.

Please test changes against a working Tutor installation before submitting them.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
