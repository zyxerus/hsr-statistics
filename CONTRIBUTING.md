# Contributing guide

## Commits

This repository uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) as a base.

### Types
- `fix`: a commit of the type `fix` patches a bug in your codebase
- `feat`: a commit of the type `feat` introduces a new feature to the codebase
- `data`: a commit of the type `data` intruduces changes in the `data/` folder
- `docs`: a commit of the type `docs` intruduces changes related to documenting
- `perf`: a commit of the type `perf` is used when the only changes were performance related
- `revert`: a commit of type `revert` can only be used when an other commit is reverted


### Structure

Every commit should follow the follwing structure:
```
<type>[optional scope]: <description>

[optional body]
```

For `revert` commits a unique format is used:
```
revert: <commit_id>

[optional reason]
```