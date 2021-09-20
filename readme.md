<!-- markdownlint-disable-file MD033-->

<!-- PROJECT LOGO -->
<br/>
<p align="center">
  <a href="https://github.com/wasi-master/todot">
    <img src="https://raw.githubusercontent.com/wasi-master/todot/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">todot</h2>

  <p align="center">
    A powerful tool to parse TODOs/FIXMEs etc. from source files
    <br />
    <a href="https://wasi-master.github.io/todot/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wasi-master/todot/blob/main/demo.md">View Demo</a>
    ·
    <a href="https://github.com/wasi-master/todot/issues">Report Bug</a>
    ·
    <a href="https://github.com/wasi-master/todot/issues">Request Feature</a>
  </p>
</p>

<p align="center">
   <a href="https://github.com/wasi-master/todot/graphs/contributors"><img src="https://img.shields.io/github/contributors/wasi-master/todot.svg?style=flat" alt="Contributors"></a>
   <a href="https://github.com/wasi-master/todot/network/members"><img src="https://img.shields.io/github/forks/wasi-master/todot.svg?style=flat" alt="Forks"></a>
   <a href="https://github.com/wasi-master/todot/stargazers"><img src="https://img.shields.io/github/stars/wasi-master/todot.svg?style=flat" alt="Stargazers"></a>
   <a href="https://github.com/wasi-master/todot/issues"><img src="https://img.shields.io/github/issues/wasi-master/todot.svg?style=flat" alt="Issues"></a>
   <a href="https://github.com/wasi-master/todot"><img src="https://img.shields.io/github/languages/code-size/wasi-master/todot.svg?style=flat" alt="Code Size"></a>
   <a href="https://github.com/wasi-master/todot/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/wasi-master/todot.svg?style=flat" alt="MIT License"></a>
   <a href="https://saythanks.io/to/arianmollik323@gmail.com"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks"></a>
   <a href="https://pypistats.org/packages/todot-python"><img src="https://img.shields.io/pypi/dm/todot-python.svg?style=flat" alt="Downloads"></a>
   <a href="https://pypi.org/project/todot-python/#history"><img src="https://img.shields.io/pypi/v/todot-python.svg" alt="Version"></a>
   <a href="https://github.com/wasi-master/todot/actions/workflows/python-app.yml"><img src="https://img.shields.io/github/workflow/status/wasi-master/todot/Python%20application.svg?label=tests" alt="Tests"></a>
   <a href="https://github.com/wasi-master/todot/actions/workflows/python-publish.yml"><img src="https://img.shields.io/github/workflow/status/wasi-master/todot/Upload%20Python%20Package.svg?label=build" alt="Build"></a>
   <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project


todot is a powerful tool to parse TODOs/FIXMEs etc. from source files\
<!-- For a demo see [demo.md](https://github.com/wasi-master/todot/blob/main/demo.md) -->

### Built With

* [python](https://www.python.org)

<!-- GETTING STARTED -->
## Getting Started

To install todot:

### Prerequisites

You'll need to have [python 3.6+](https://www.python.org) installed in order to use the extension

### Installation

You'll need to install [python](https://www.python.org) in order to use the extension

Currently there are two ways to install todot (the `[rich]` part adds rich terminal support)

* Installing via pip
  1. Directly installing via pip (Recommended)

     ```sh
     pip install todot-python[rich]
     ```

     or

     ```sh
     pip install todot-python
     ```

  2. Installing using pip and git

     ```sh
     pip install "todot-python[rich] @ git+https://github.com/wasi-master/todot.git"
     ```

     or

     ```sh
     pip install git+https://github.com/wasi-master/todot.git
     ```

* Cloning then installing
  1. Clone the repo

     ```sh
     git clone https://github.com/wasi-master/todot.git
     ```

  2. Install using pip

     ```sh
     pip install .[rich]
     ```

     or

     ```sh
     pip install .
     ```


<!-- USAGE EXAMPLES -->
## Usage

Go in a terminal and run

```sh
todot
```

There are more options to configure that can be found in the [Documentation](https://wasi-master.github.io/todot#Configuration)

_For more examples such as github workflow, configuring via file, please refer to the [Documentation](https://wasi-master.github.io/todot/)_

<!-- ROADMAP -->
## Roadmap

See the [todo list](https://github.com/wasi-master/todot/blob/main/TODO.md) for a list of features yet to be added (and known issues).
Also see the [open issues](https://github.com/wasi-master/todot/issues) issues.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](license.md) for more information.

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/wasi-master/todot](https://github.com/wasi-master/todot)

Discord: [Wasi Master#6969](https://discord.com/users/723234115746398219)

Email: [arianmollik323@gmail.com](mailto:arianmollik323@gmail.com)
