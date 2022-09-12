## v2.0.0 (2022-09-12)

### Feat

- updated the readme
- **presets**: new vue(js and ts) preset
- **presets**: new sveltekit(js only) preset
- **presets**: new svelte(js and ts) presets
- **presets**: new [astro](https://astro.build) preset
- **extensions**: updated extension api to match preset and package manager api
- **api**: migrated all presets to new api
- **api**: migrated all js presets to new api
- **api**: migrate the ts presets to new api
- **api**: migrate old js presets to new api
- **api**: added new base classes for package managers and presets

### Fix

- fix critical bug
- update main cli script to new api for all presets
- **api**: improved checking for package manager installation in new api
- added exception handling and proper error messages and improved detection
- **import**: fix relative import paths

## v1.4.0 (2022-08-11)

### Feat

- **commands**: added new command to migrate and formatted all files
- **commands**: new list command and minor improvements
- **commands**: add new flag to config command and renamed list command to tree
- **commands**: updated get command and new remove command

## v1.3.0 (2022-06-17)

### Feat

- **node**: ts support for node projects
- **node**: now allows project generation of nodejs
- **extensions**: include rrpmpkg as a dependency
- Virtual Environment support
- Pnpm create-react-app support

### Fix

- Remote useless return statements
- Update Badge
- Fix bug where package manager was not found even when it existed

## v1.2.0 (2022-06-06)

## v1.1.0 (2022-06-04)
