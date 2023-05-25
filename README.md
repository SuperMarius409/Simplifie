# Simplifique [1.0.0](https://github.com/SuperMarius409/Simplifie)

<img align="right" height="256" src="https://github.com/SuperMarius409/Simplifie/blob/main/fisiere/project/computer/images/icon.png"/>

KivyMD is a collection of Material Design compliant widgets for use with
[Kivy](http://kivy.org), a framework for cross-platform, touch-enabled
graphical applications.

The project's goal is to approximate Google's
[Material Design spec](https://material.io/design/introduction/) as close as
possible without sacrificing ease of use. This library is a fork of the
[KivyMD project](https://gitlab.com/kivymd/KivyMD). We found the strength and
brought this project to a new level.

Join the project! Just fork the project, branch out and submit a pull request
when your patch is ready. If any changes are necessary, we'll guide you through
the steps that need to be done via PR comments or access to your for may be
requested to outright submit them.

If you wish to become a project developer (permission to create branches on the
project without forking for easier collaboration), have at least one PR
approved and ask for it. If you contribute regularly to the project the role
may be offered to you without asking too.

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Repository size](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://github.com/SuperMarius409)

## Installation

```bash
pip install kivymd==1.1.1
```
## Simplifie

Numele Echipei: Simplifie

Numele Aplicatiei: Simplifique

Membri Echipei: Radulescu Marius (partea tehnica), Vacaru Stefania(partea de design si cu ideea)

Scoala: Colegiul National Militar "Tudor Vladimirescu" 

### Dependencies:

- [Kivy](https://github.com/kivy/kivy) >= 2.2.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.7+](https://www.python.org/)
- [Pillow](https://github.com/python-pillow/Pillow/)
- [MaterialColor](https://github.com/T-Dynamos/materialyoucolor-pyhton)

### How to install

Command [above](#installation) will install latest release version of KivyMD from 
[PyPI](https://pypi.org/project/kivymd).

If you want to install development version from 
[master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```bash
pip install https://github.com/kivymd/KivyMD/archive/master.zip
```

**_Tip_**: Replace `master.zip` with `<commit hash>.zip` (eg `51b8ef0.zip`) to
download KivyMD from specific commit.

Also you can install manually from sources. Just clone the project and run pip:

```bash
git clone https://github.com/kivymd/KivyMD.git --depth 1
cd KivyMD
pip install .
```

**_Speed Tip_**: If you don't need full commit history (about 1.14 GiB), you can
use a shallow clone (`git clone https://github.com/kivymd/KivyMD.git --depth 1`)
to save time. If you need full commit history, then remove `--depth 1`.

### How to fix a shader bug on an android device

Use `Kivy` from master branch or `Kivy` >= `2.2.0` and `KivyMD` (from master branch):

```bash
pip install https://github.com/kivy/kivy/archive/master.zip
pip install https://github.com/kivymd/KivyMD/archive/master.zip
```

And use with `Buildozer`:

```ini
requirements = kivy==master, https://github.com/kivymd/KivyMD/archive/master.zip
```

### How to use with [Buildozer](https://github.com/kivy/buildozer)

```ini
requirements = kivy==2.1.0, kivymd==1.1.1
```

This will download latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd).

If you want to use development version from [master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```ini
requirements = kivy==2.1.0, https://github.com/kivymd/KivyMD/archive/master.zip
```

Do not forget to run `buildozer android clean` or remove `.buildozer` directory
before building if version was updated (Buildozer doesn't update already
downloaded packages).

#### On Linux

- Use Buildozer [directly](https://github.com/kivy/buildozer#installing-buildozer-with-target-python-3-default) 
  or via [Docker](https://github.com/kivy/buildozer/blob/master/Dockerfile).

#### On Windows 10

- Install [Ubuntu WSL](https://ubuntu.com/wsl) and follow [Linux steps](#On-Linux).

#### Build automatically via GitHub Actions

- Use [ArtemSBulgakov/buildozer-action@v1](https://github.com/ArtemSBulgakov/buildozer-action)
  to build your packages automatically on push or pull request.
- See [full workflow example](https://github.com/ArtemSBulgakov/buildozer-action#full-workflow).

### How to use with [kivy-ios](https://github.com/kivy/kivy-ios)

```bash
toolchain build python3 kivy pillow
toolchain pip install --no-deps kivymd
```

## Documentation

- See documentation at https://kivymd.readthedocs.io
- Wiki with examples of using KivyMD widgets: https://github.com/kivymd/KivyMD/wiki

### Demos

<p align="center">
  <a href="https://www.youtube.com/watch?v=4er9b6TH_TA">
    <img 
        width="600" 
        src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-kitchen-sink.png" 
        title="Click to watch demo application of the KivyMD library widgets"
    >
  </a>
</p>

[Kitchen sink](https://github.com/kivymd/KitchenSink) app demonstrates every KivyMD widget.
You can see how to use widget in code of app.