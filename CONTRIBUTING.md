# Contributing to FAST-HEP

Thank you for your interest in contributing to FAST-HEP!

FAST-HEP is a toolkit for building declarative High Energy Physics (HEP) analyses. It is developed as a collection of focused packages, with some components designed to be useful beyond HEP.

Contributions of all sizes are welcome, including:

* bug reports and feature requests
* documentation fixes and improvements
* tutorials and workflow examples
* tests and bug fixes
* new features and infrastructure
* larger architectural improvements

You do not need to be familiar with the entire FAST-HEP toolkit to contribute to an individual package.

## Getting started

If you have found a bug, have an idea for a feature, or are unsure where a change belongs, start by opening an [issue](https://github.com/FAST-HEP/fasthep/issues) or asking in [GitHub Discussions](https://github.com/FAST-HEP/fasthep/discussions).

For small and self-contained changes, such as typo fixes or straightforward documentation improvements, you can open a pull request directly.

For substantial features, refactors, or architectural changes, please discuss the proposal before investing significant implementation effort.

A typical contribution looks like:

1. Find or open an issue describing the change.
2. Identify the FAST-HEP package responsible for it.
3. Create a branch in the relevant repository.
4. Implement and test the change.
5. Run the repository's local checks.
6. Open a pull request and describe what changed and why.
7. Review and iterate.

Where practical, prefer small, focused pull requests over large changes containing unrelated work.

## Choosing a package

FAST-HEP separates different responsibilities across focused packages:

| Package             | Responsibility                                                       |
| ------------------- | -------------------------------------------------------------------- |
| `fasthep-flow`      | Workflow description, compilation, planning, and execution           |
| `fasthep-carpenter` | HEP analysis transforms, histogramming, and columnar data processing |
| `fasthep-curator`   | Dataset inspection, metadata, provenance, and diagnostics            |
| `fasthep-render`    | Plotting, reports, and visualisation                                 |
| `fasthep-cli`       | Unified command-line interface                                       |
| `fasthep-toolbench` | Shared, domain-independent utilities                                 |
| `fasthep-workshop`  | Tutorials, examples, and training material                           |

If your change affects several packages, use the `fasthep-dev` integration workspace.

If you are unsure where a contribution belongs, open an issue or discussion in the `fasthep` repository.

## Development environment

FAST-HEP uses [Pixi](https://pixi.sh/) to provide reproducible development environments. Python 3.11 or newer is supported.

After cloning the package you want to work on, most repositories can be set up with:

```bash
pixi install
```

The complete local CI suite can usually be run with:

```bash
pixi run ci
```

Individual checks are also commonly available:

```bash
pixi run lint
pixi run typecheck
pixi run test
```

FAST-HEP commonly uses:

* `ruff` for linting and formatting checks
* `mypy` for static type checking
* `pytest` for testing
* `pre-commit` for repository checks
* GitHub Actions for continuous integration

Check the individual repository for any package-specific development instructions.

### Working across packages

The `fasthep-dev` workspace provides a development environment for:

* cross-package integration
* shared tooling
* toolkit-level testing
* coordinated release validation

Contributors making changes across multiple FAST-HEP packages are encouraged to use `fasthep-dev`.

## Pull requests

Pull requests should explain:

* what changed
* why the change is needed
* any important implementation or design decisions
* how the change was tested

New functionality should generally include appropriate tests. Bug fixes should include regression tests where practical.

Tests should be deterministic, avoid unnecessary external dependencies and hidden global state, and prefer realistic fixtures over excessive mocking where practical.

## Coding guidelines

FAST-HEP prioritises readability, maintainability, explicit interfaces, strong typing, and testability.

When contributing code:

* use descriptive names
* keep functions focused
* prefer composition over tightly coupled implementations
* avoid unnecessary abstractions
* prefer explicit behaviour over implicit magic
* add tests for new functionality
* keep general workflow infrastructure separate from domain-specific analysis logic

These principles are intended to keep individual packages understandable and independently maintainable.

## Documentation and examples

Documentation improvements are highly valued. Useful contributions include:

* examples and tutorials
* API documentation
* workflow diagrams
* migration guides
* debugging notes
* fixes to unclear or outdated documentation

When writing documentation:

* keep examples minimal enough to understand
* prefer realistic workflows
* document design intent, not only implementation details
* avoid committing generated caches, build outputs, or large derived artifacts unless they are explicitly required

### Workflow examples

Workflow examples should use public or open data where possible.

Data hosted on services such as CERN EOS or CERNBox may also be used when it is intended for redistribution.

Examples should:

* include provenance and source information
* be reproducible where practical
* avoid committing large binary files directly to repositories

Additional tutorial and example conventions are documented by `fasthep-workshop`.

## AI-assisted contributions

AI-assisted contributions are welcome, but contributors remain responsible for the code and documentation they submit.

Contributors should understand and review generated changes, validate their correctness, ensure relevant tests pass, and make sure the implementation is consistent with FAST-HEP's design principles.

For substantial AI-generated or AI-assisted changes, pull requests should briefly describe:

* what was generated or assisted by AI
* what was manually reviewed or modified
* important design decisions
* known limitations, assumptions, or areas requiring additional review

AI tools should assist engineering work rather than replace contributor understanding or reviewer accountability.

Reviewers may ask for changes when generated code cannot be reasonably explained, introduces unnecessary or unclear abstractions, or appears not to have been adequately reviewed.

## Design principles

FAST-HEP separates general workflow infrastructure from specialised analysis capabilities.

In particular, responsibilities such as workflow orchestration, HEP analysis logic, rendering, metadata management, and command-line interfaces live in focused packages with explicit interfaces between them.

This separation supports independent package development, experiment-specific extensions, and reuse of general components outside HEP.

Contributors should preserve these boundaries where practical. If a change appears to require crossing them, discussing the design before implementation is encouraged.

## Releases

FAST-HEP packages are released independently.

The `fasthep` meta-package provides curated, compatible combinations of packages for users of the complete toolkit.

The `fasthep-dev` workspace supports integration testing and coordinated validation across packages.

## Getting help

Questions about using or contributing to FAST-HEP are welcome in [GitHub Discussions](https://github.com/FAST-HEP/fasthep/discussions).

Bug reports and feature requests can be submitted through [GitHub Issues](https://github.com/FAST-HEP/fasthep/issues).

If you are unsure whether something is a bug, feature request, or general question, starting a discussion is perfectly fine.

## License

By contributing to FAST-HEP, you agree that your contributions will be licensed under the BSD-3-Clause license used by the project.
