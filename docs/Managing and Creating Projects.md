# Managing and Creating Projects

Managing and creating projects using presets with RRPM

## Available Presets

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

> **Note** Unchecked boxes signify they are still a work in progress.

## Creating Projects

> **Warning** Certain projects require certain tools to be installed for them to work.

We will use the rrpm create command to generate projects based on the preset and variation we select as shown below.

![gif](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXgiQENn1M5zzSjVVXASX%2Fuploads%2FpOsLrfIqsfyOIWShqBaQ%2Frrpm.gif?alt=media&token=43d589ff-7d56-485e-b097-75b3a9c21558)

### Usage

```bash
Usage: python -m rrpm create [OPTIONS] NAME

  Generate a project from any of the presets and/or its variations

Arguments:
  NAME  [required]

Options:
  --src / --no-src  [default: no-src]
  --help            Show this message and exit.
```

- `[NAME]`: Name of the project. Required for all presets.
- `--src` / `--no-src`: Applicable for poetry projects only.