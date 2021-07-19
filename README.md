<p align="center">
    <img src="https://raw.githubusercontent.com/guilatrova/tryceratops/main/img/logo.png">
</p>

<h2 align="center">Manage your exceptions in Python like a PRO</h2>

<p align="center">
  <a href="https://pypi.org/project/tryceratops/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/tryceratops"/>
  </a>

  <a href="https://pepy.tech/project/tryceratops/">
    <img alt="Downloads" src="https://static.pepy.tech/personalized-badge/tryceratops?period=total&units=international_system&left_color=grey&right_color=blue&left_text=%F0%9F%A6%96%20Downloads"/>
  </a>

  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
  </a>

  <a href="https://github.com/guilatrova/tryceratops">
    <img alt="try/except style: tryceratops" src="https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black" />
  </a>

  <a href="https://open.vscode.dev/guilatrova/tryceratops">
    <img alt="Open in Visual Studio Code" src="https://open.vscode.dev/badges/open-in-vscode.svg"/>
  </a>


</p>

Currently in BETA.
Inspired by [this blog post](https://blog.guilatrova.dev/handling-exceptions-in-python-like-a-pro/).

I shared [the building process of this tool here](https://blog.guilatrova.dev/project-tryceratops/).

> “For those who like dinosaurs 🦖 and clean try/except ✨ blocks.”

- [Installation and usage](#installation-and-usage)
  - [Installation](#installation)
  - [Usage](#usage)
  - [`flake8` Plugin](#flake8-plugin)
- [Violations](#violations)
  - [Ignoring violations](#ignoring-violations)
  - [Configuration](#configuration)
- [Pre-commit](#pre-commit)
- [Show your style](#show-your-style)
- [Extra Resources](#extra-resources)
- [License](#license)
- [Credits](#credits)

---

## Installation and usage

### Installation

```
pip install tryceratops
```

### Usage

```
tryceratops [filename or dir...]
```

You can enable experimental analyzers by running:

```
tryceratops --experimental [filename or dir...]
```

You can ignore specific violations by using: `--ignore TCXXX` repeatedly:

```
tryceratops --ignore TC201 --ignore TC202 [filename or dir...]
```

You can exclude dirs by using: `--exclude dir/path` repeatedly:

```
tryceratops --exclude tests --exclude .venv [filename or dir...]
```

![example](https://raw.githubusercontent.com/guilatrova/tryceratops/main/img/tryceratops-example2.gif)

### [`flake8`](https://github.com/PyCQA/flake8) Plugin

🦖 Tryceratops is also a plugin for `flake8`, so you can:

```
❯ flake8 --select TC src/tests/samples/violations/call_raise_vanilla.py
src/tests/samples/violations/call_raise_vanilla.py:13:9: TC002 Create your own exception
src/tests/samples/violations/call_raise_vanilla.py:13:9: TC003 Avoid specifying long messages outside the exception class
src/tests/samples/violations/call_raise_vanilla.py:21:9: TC201 Simply use 'raise' without specifying exception object again
```

## Violations

All violations and its descriptions can be found in [docs](https://github.com/guilatrova/tryceratops/tree/main/docs/violations).

### Ignoring violations

If you want to ignore a violation in a specific file, you can either:

- Add a comment with `notc` to the top of the file you want to ignore
- Add a comment with `notc` to the line you want to ignore
- Add a comment with `notc: CODE` to the line you want to ignore a specific violation

Example:

```py
def verbose_reraise_1():
    try:
        a = 1
    except Exception as ex:
        raise ex  # notc: TC202
```

### Configuration

You can set up a `pyproject.toml` file to set rules.
This is useful to avoid reusing the same CLI flags over and over again and helps to define the structure of your project.

Example:

```toml
[tool.tryceratops]
exclude = ["samples"]
ignore = ["TC002", "TC200", "TC300"]
experimental = true
```

CLI flags always overwrite the config file.

## Pre-commit

If you wish to use pre-commit, add this:

```yaml
  - repo: https://github.com/guilatrova/tryceratops
    rev: v0.2.5
    hooks:
      - id: tryceratops
```

## Show your style

[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)

Add this fancy badge to your project's `README.md`:

```md
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)
```

## Extra Resources

If you want to read more about:

- [How to structure exceptions in Python 🐍 🏗️ 💣](https://blog.guilatrova.dev/how-to-structure-exception-in-python-like-a-pro/)
- [Book: Effective Python](https://amzn.to/3bEVHpG)

## License

MIT

## Credits

Thanks to God for the inspiration 🙌 ☁️ ☀️

Logo icon was made by [https://www.freepik.com](Freepik)

The [black](https://github.com/psf/black) project for insights.
