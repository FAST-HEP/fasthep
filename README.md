# fasthep

[![CI](https://github.com/FAST-HEP/fasthep/actions/workflows/ci.yml/badge.svg)](https://github.com/FAST-HEP/fasthep/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/fasthep)](https://pypi.org/project/fasthep/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fasthep)](https://pypi.org/project/fasthep/)
[![Documentation Status](https://readthedocs.org/projects/fasthep/badge/?version=latest)](https://fasthep.readthedocs.io/en/latest/)
[![Discussions](https://img.shields.io/static/v1?label=Discussions\&message=Ask\&color=blue\&logo=github)](https://github.com/FAST-HEP/fasthep/discussions)

<p align="center">
  <a href="https://github.com/FAST-HEP/fasthep">
    <picture>
      <source
        media="(prefers-color-scheme: dark)"
        srcset="https://raw.githubusercontent.com/FAST-HEP/logos-etc/master/fast-hep-white.png"
      >
      <source
        media="(prefers-color-scheme: light)"
        srcset="https://raw.githubusercontent.com/FAST-HEP/logos-etc/master/fast-hep-black.png"
      >
      <img
        alt="FAST-HEP"
        src="https://raw.githubusercontent.com/FAST-HEP/logos-etc/master/fast-hep-black.png"
        width="500"
      >
    </picture>
  </a>
</p>

`fasthep` is the meta package for the FAST-HEP ecosystem.

It provides curated installation profiles for compatible FAST-HEP packages and acts as the primary user-facing installation entry point.

## What is FAST-HEP?

FAST-HEP is a modular ecosystem for declarative High Energy Physics workflows.

The ecosystem is split into focused packages:

* `fasthep-flow`

  * workflow compilation and orchestration

* `fasthep-carpenter`

  * analysis transforms and histogramming

* `fasthep-curator`

  * dataset inspection and validation

* `fasthep-render`

  * plotting and report generation

* `fasthep-cli`

  * unified command-line interface

* `fasthep-toolbench`

  * shared utilities and UX helpers

* `fasthep-workshop`

  * examples and tutorials

The goal is to keep:

* workflow orchestration
* analysis logic
* rendering
* metadata handling
* user tooling

cleanly separated and independently evolvable.

## Installation profiles

`fasthep` provides optional dependency groups for different usage profiles.

### Basic workflow tools

Installs:

* `fasthep-flow`
* `fasthep-cli`

```bash
pip install "fasthep[basic]"
```

### HEP analysis stack

Installs:

* `fasthep-flow`
* `fasthep-cli`
* `fasthep-curator`
* `fasthep-carpenter`
* `fasthep-render`

```bash
pip install "fasthep[hep]"
```

### Full ecosystem

Installs:

* all HEP analysis packages
* shared utilities

```bash
pip install "fasthep[full]"
```

### Workshop/tutorial environment

Installs workshop examples and tutorial material.

```bash
pip install "fasthep[workshop]"
```

## Verified compatibility bundles

The purpose of the `fasthep` meta package is to provide:

* known-good package combinations
* coordinated ecosystem releases
* compatibility-tested dependency sets

Individual FAST-HEP packages evolve independently.

The `fasthep` meta package is intended to represent a verified integration layer across the ecosystem.

## Development status

FAST-HEP is currently in active pre-alpha development.

Some optional dependencies currently use Git-based installation while packages are being split and published independently.

These direct references are temporary and will be replaced with standard PyPI version pins once the ecosystem stabilizes.

## Development environment

Using Pixi:

```bash
pixi install
pixi run ci
```

## Documentation

Main FAST-HEP documentation:

* [https://fast-hep.github.io](https://fast-hep.github.io)

Package/API documentation:

* [https://fasthep.readthedocs.io/en/latest/](https://fasthep.readthedocs.io/en/latest/)

## Repository

Main project repository:

* [https://github.com/FAST-HEP/fasthep](https://github.com/FAST-HEP/fasthep)

## Contributing

Contribution guidelines, development setup, and project-wide documentation are maintained centrally in the main FAST-HEP repository.

## Release model

FAST-HEP packages are released independently.

The `fasthep` meta package is used to:

* aggregate compatible package sets
* verify ecosystem integration
* provide stable installation profiles

This separation allows:

* faster iteration on individual packages
* coordinated compatibility releases
* gradual ecosystem stabilization

## Status

FAST-HEP is currently in active pre-alpha development.

Interfaces, dependency layouts, and installation profiles may evolve rapidly while the ecosystem stabilizes.
