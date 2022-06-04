# rrpm

**rrpm** is the all-in-one project and remote repository management tool. A simple CLI tool that supports project
generation for multiple languages, along with support for generating projects using different package managers and/or
environments

## Installation

`rrpm` can be installed from PyPI

```bash
pip install rrpm
```

## Usage

```bash
Usage: python -m rrpm [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  create  Generate a project from any of the presets and/or its variations
  get     Clone a remote repository to directory specified in config
  list    List all cloned repositories and generated projects
```

## Presets
 - [ ] Python
   - [x] Pip
     - [x] Python Package
     - [x] FastAPI
     - [x] Flask
   - [x] Poetry
     - [x] Python Package
     - [x] FastAPI
     - [x] Flask
   - [ ] Virtual Environments
     - [ ] Python Package
     - [ ] FastAPI
     - [ ] Flask
 - [ ] JavaScript
    - [ ] NPM
      - [ ] NodeJS
      - [x] ReactJS
        - [x] create-react-app
        - [x] Vite
      - [x] NextJS
    - [ ] Yarn
      - [ ] NodeJS
      - [x] ReactJS
        - [x] create-react-app
        - [x] Vite
      - [x] NextJS
    - [ ] Pnpm
      - [ ] NodeJS
      - [ ] ReactJS
        - [ ] create-react-app
        - [x] Vite
      - [x] NextJS
 - [ ] TypeScript
     - [ ] NPM
       - [ ] NodeJS
       - [x] ReactJS
         - [x] create-react-app
         - [x] Vite
       - [x] NextJS
     - [ ] Yarn
       - [ ] NodeJS
       - [x] ReactJS
         - [x] create-react-app
         - [x] Vite
       - [x] NextJS
     - [ ] Pnpm
       - [ ] NodeJS
       - [ ] ReactJS
         - [ ] create-react-app
         - [x] Vite
       - [x] NextJS

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)