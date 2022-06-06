# Managing Remote Repositories

Managing remote repositories with RRPM

## Cloning Remote Repositories

Remote Git repositories such as those hosted on GitHub or GitLab can be cloned by using the rrpm get command as shown below.

```bash
$ python -m rrpm get github.com/pybash1/rrpm # notice that the https:// and .git are optional.
Fetching GitHub Repository
Successfully cloned repository in github.com/pybash1/rrpm
```

The above command clones the pybash1/rrpm repository to the directory %USERPROFILE%\Projects on Windows and ~/Projects on Unix by default. this can be changed in the config.toml file.

### Usage
```bash
Usage: python -m rrpm get [OPTIONS] URL

  Clone a remote repository to directory specified in config

Arguments:
  URL  [required]

Options:
  --help  Show this message and exit.
```

## Listing Cloned Repositories

The rrpm list command can be used to display a tree of the of the projects cloned to the root directory as shown below

```bash
$ python -m rrpm list
C:\Users\mitra\Projects
  |- github.com
      |- CutCode-org
          |- CutCode-svelte
      |- github
          |- gitignore
      |- pastegram
          |- backend
      |- pybash1
          |- pm
          |- portfolio
          |- pybash1
          |- rrpm
```

The root directory is as per the config.toml file.

### Usage

```bash
Usage: python -m rrpm list [OPTIONS]

  List all cloned repositories and generated projects

Options:
  --help  Show this message and exit.
```