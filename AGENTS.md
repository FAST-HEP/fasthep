# fasthep Metapackage Agent Instructions

This repository owns the `fasthep` metapackage: the user-facing installation
entry point for compatible FAST-HEP releases. It should stay useful when cloned
and developed independently.

## Ownership

This repository owns:

- the minimal `fasthep` installation entry point;
- optional installation bundles under `[project.optional-dependencies]`;
- compatible released-package constraints for FAST-HEP packages;
- installation, packaging, distribution, and import smoke tests;
- the shared `CONTRIBUTING.md` referenced by companion repositories.

This repository does not own implementations from `fasthep-flow`,
`fasthep-carpenter`, `fasthep-curator`, `fasthep-render`, `fasthep-cli`,
`fasthep-distributed`, `fasthep-toolbench`, or `fasthep-workshop`. Do not add
implementation code here merely to coordinate those packages.

## Installation Contracts

The default installation is intentionally minimal. `pyproject.toml` currently
has no base runtime dependencies, so `pip install fasthep` should import the
metapackage without importing optional FAST-HEP packages.

Current extras are public user-facing contracts:

- `basic` - workflow and CLI entry point users; installs `fasthep-flow` and
  `fasthep-cli`.
- `hep` - ordinary HEP analysis users; installs Flow, CLI, Curator, Carpenter,
  and Render.
- `full` - ecosystem users who also need shared helper utilities; installs the
  `hep` stack plus `fasthep-toolbench`.
- `workshop` - tutorial and training users; installs `fasthep-workshop`.
- `test` - repository test dependencies for this metapackage.

When changing extras, update installation documentation and tests. Verify that
each extra resolves and exposes its intended capabilities, and avoid importing
optional packages during a minimal installation.

Use compatible released distributions in dependency declarations. Do not replace
released constraints with workspace paths, editable dependencies, or source-tree
shortcuts in this repository. Unreleased source-level integration across
multiple local repositories belongs in `fasthep-dev`.

## Boundaries

- Flow owns workflow compilation, plans, runtime orchestration, registries, and
  backend contracts.
- Carpenter owns analysis operations, awkward-array transforms, ROOT
  sources/sinks, selections, cutflows, and histogram filling.
- Curator owns metadata inspection, schema snapshots, diagnostics, validation,
  provenance, and environment/resource evidence.
- Render owns plots, reports, styles, and rendered presentation.
- CLI owns the `fasthep` command-line interface, routing, arguments, diagnostics,
  and exit behaviour.
- Distributed owns Dask, HTCondor, scheduler integration, staging, worker
  environments, and distributed execution implementation.

Installed-release compatibility and import smoke tests may grow here over time.
Source-level integration across uncommitted repositories remains owned by
`fasthep-dev`.

## Important Locations

- `pyproject.toml` - package metadata, Python support, extras, versioning,
  build configuration, pytest, and Ruff settings.
- `pixi.toml` - local development tasks and Python compatibility environments.
- `src/fasthep/__init__.py` - minimal import surface and version export.
- `src/fasthep/_version.py` - generated Hatch-VCS version module.
- `src/fasthep/_version.pyi` - type stub for the generated version module.
- `tests/test_imports.py` - minimal import smoke test.
- `README.md` - user-facing installation profiles and metapackage overview.
- `CONTRIBUTING.md` - shared human-facing contribution guide for FAST-HEP.
- `.github/workflows/ci.yml` and `.github/workflows/cd.yml` - durable package
  check, build, distribution-check, and publish wiring.

## Commands

Install and run tasks from the repository root:

```bash
pixi install
pixi run format
pixi run lint
pixi run lint-fix
pixi run test
pixi run smoke
pixi run build
pixi run check-dist
pixi run check
pixi run ci
```

`check` runs `lint`, `test`, and `smoke`. `ci` runs `check`, `build`, and
`check-dist`. Build before running `check-dist` so `dist/*` exists. The Pixi
compatibility environments are `py311`, `py313`, and `py314`; use the default
environment for routine work unless validating a specific Python version.

## Packaging and Compatibility

- Supported Python is declared in `pyproject.toml` as `>=3.11`; classifiers list
  Python 3.11, 3.12, and 3.13, while Pixi also defines a Python 3.14
  compatibility environment.
- Versioning is provided by Hatch-VCS. Do not edit generated version files by
  hand.
- Keep dependency pins compatible across extras. Avoid unnecessary duplication
  between the base package and extras, and do not add base dependencies unless
  they are needed for the minimal metapackage import.
- Treat extra names and membership as public API. Changing them can break user
  installation commands, tutorials, CI jobs, and downstream environment files.
- Keep distribution metadata valid with `pixi run build` and
  `pixi run check-dist` before release-oriented changes.

## Testing Expectations

- Keep routine tests lightweight and independent of network access, batch
  infrastructure, local sibling repositories, and large datasets.
- Minimal-install tests should confirm `import fasthep` and version access
  without importing optional companion packages.
- Extra-resolution tests should use released package constraints and check that
  each bundle exposes the expected installed capabilities.
- Installation documentation and tests should change together when extras,
  Python support, package metadata, or release constraints change.

## CONTRIBUTING.md

`CONTRIBUTING.md` remains the shared human-facing contribution guide. This
`AGENTS.md` adds operational guidance for agents and should reference that guide
rather than duplicating it. Preserve companion-repository links to
`CONTRIBUTING.md`; if a link is stale, report it instead of editing another
repository in this task.
