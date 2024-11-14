# boa favorites

This is from the [Cyfrin Updraft Vyper Course]().

- [boa favorites](#boa-favorites)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Optional prerequisites](#optional-prerequisites)
    - [Optional Gitpod or CodeSpaces](#optional-gitpod-or-codespaces)
  - [Installation](#installation)
    - [uv](#uv)
    - [pip/python](#pippython)
  - [Quickstart](#quickstart)
    - [1. Setup anvil node](#1-setup-anvil-node)
    - [2. In a new terminal, run the script](#2-in-a-new-terminal-run-the-script)
- [Maintainer notes](#maintainer-notes)
  - [Build a new requirements.txt](#build-a-new-requirementstxt)


# Getting Started

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
  - You'll know you've done it right if you can run `uv --version` and see a version number.
- [git](https://git-scm.com/)
  - You'll know you've done it right if you can run `git --version` and see a version number.
- [anvil](https://book.getfoundry.sh/anvil/)
  - You'll know you've done it right if you can run `anvil --version` and see an output like `anvil 0.2.0 (fdd321b 2024-10-15T00:21:13.119600000Z)`

### Optional prerequisites

If you're an advanced python user, you can use virtual environments and classic python/pip to work here.

- [python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

### Optional Gitpod or CodeSpaces

If you can't or don't want to run and install locally, you can work with this repo in Gitpod. If you do this, you can skip the `clone this repo` part.

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://gitpod.io/#github.com/cyfrin/boa-favorites-cu">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in Gitpod" style="height: 50px;">
  </a>
  <a href="https://github.dev/Cyfrin/boa-favorites-cu">
    <img src="https://www.svgrepo.com/show/347707/codespaces.svg" alt="Open in CodeSpaces" style="height: 50px;">
  </a>
</div>


## Installation

```bash
git clone https://github.com/cyfrin/boa-favorites-cu
cd boa-favorites-cu
```

### uv 

```bash
uv sync
```

### pip/python

```bash
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Quickstart

### 1. Setup anvil node

```bash
anvil
```

### 2. In a new terminal, run the script

```bash
uv run deploy_favorites.py # uv
# or
python deploy_favorites.py # pip/python
```

# Maintainer notes

If you're a student, ignore this section!

## Build a new requirements.txt

```bash
uv pip compile pyproject.toml -o requirements.txt
```