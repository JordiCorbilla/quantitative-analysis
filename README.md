# Quantitative Analysis

Algorithmic trading and Quantitative Analysis

## 1) Setup
To execute all the code in this repo, we'll use [Anaconda3](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe) and [Spyder IDE](https://www.spyder-ide.org/) which will allow us to create virtual environments. 

Once Anaconda is installed, launch the command line with **Admin** permissions. 

Below is the list of packages to install and commands to run on the Anaconda console: 

### 1.1) Updating Anaconda

```cmd
conda update -n base conda
```

```cmd
(base) C:\Users\thund>conda update -n base conda
Solving environment: done

## Package Plan ##

  environment location: C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.8.3                |           py36_0         3.1 MB
    libcurl-7.71.1             |       h2a8f88b_1         289 KB
    qt-5.9.7                   |   vc14h73c81de_0        92.3 MB
    tqdm-4.47.0                |             py_0          62 KB
    cryptography-2.9.2         |   py36h7a1dbc1_0         586 KB
    vc-14.1                    |       h0510ff6_4           6 KB
    certifi-2020.6.20          |           py36_0         160 KB
    libpng-1.6.37              |       h2a8f88b_0         598 KB
    sqlite-3.32.3              |       h2a8f88b_0         1.3 MB
    pycurl-7.43.0.5            |   py36h7a1dbc1_0          69 KB
    libssh2-1.9.0              |       h7a1dbc1_1         218 KB
    openssl-1.1.1g             |       he774522_0         5.8 MB
    ca-certificates-2020.6.24  |                0         165 KB
    curl-7.71.1                |       h2a8f88b_1         132 KB
    conda-package-handling-1.6.1|   py36h62dcd97_0         673 KB
    krb5-1.18.2                |       hc04afaa_0         848 KB
    vs2015_runtime-14.16.27012 |       hf0eaf9b_3         2.4 MB
    ------------------------------------------------------------
                                           Total:       108.5 MB

The following NEW packages will be INSTALLED:

    conda-package-handling: 1.6.1-py36h62dcd97_0
    krb5:                   1.18.2-hc04afaa_0
    tqdm:                   4.47.0-py_0

The following packages will be UPDATED:

    ca-certificates:        2018.03.07-0            --> 2020.6.24-0
    certifi:                2018.4.16-py36_0        --> 2020.6.20-py36_0
    conda:                  4.5.4-py36_0            --> 4.8.3-py36_0
    cryptography:           2.2.2-py36hfa6e2cd_0    --> 2.9.2-py36h7a1dbc1_0
    curl:                   7.60.0-h7602738_0       --> 7.71.1-h2a8f88b_1
    libcurl:                7.60.0-hc4dcbb0_0       --> 7.71.1-h2a8f88b_1
    libpng:                 1.6.34-h79bbb47_0       --> 1.6.37-h2a8f88b_0
    libssh2:                1.8.0-hd619d38_4        --> 1.9.0-h7a1dbc1_1
    openssl:                1.0.2o-h8ea7d77_0       --> 1.1.1g-he774522_0
    pycurl:                 7.43.0.1-py36h74b6da3_0 --> 7.43.0.5-py36h7a1dbc1_0
    qt:                     5.9.5-vc14he4a7d60_0    --> 5.9.7-vc14h73c81de_0
    sqlite:                 3.23.1-h35aae40_0       --> 3.32.3-h2a8f88b_0
    vc:                     14-h0510ff6_3           --> 14.1-h0510ff6_4
    vs2015_runtime:         14.0.25123-3            --> 14.16.27012-hf0eaf9b_3

Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-4.8.3          |  3.1 MB | ############################################################################## | 100%
libcurl-7.71.1       |  289 KB | ############################################################################## | 100%
qt-5.9.7             | 92.3 MB | ############################################################################## | 100%
tqdm-4.47.0          |   62 KB | ############################################################################## | 100%
cryptography-2.9.2   |  586 KB | ############################################################################## | 100%
vc-14.1              |    6 KB | ############################################################################## | 100%
certifi-2020.6.20    |  160 KB | ############################################################################## | 100%
libpng-1.6.37        |  598 KB | ############################################################################## | 100%
sqlite-3.32.3        |  1.3 MB | ############################################################################## | 100%
pycurl-7.43.0.5      |   69 KB | ############################################################################## | 100%
libssh2-1.9.0        |  218 KB | ############################################################################## | 100%
openssl-1.1.1g       |  5.8 MB | ############################################################################## | 100%
ca-certificates-2020 |  165 KB | ############################################################################## | 100%
curl-7.71.1          |  132 KB | ############################################################################## | 100%
conda-package-handli |  673 KB | ############################################################################## | 100%
krb5-1.18.2          |  848 KB | ############################################################################## | 100%
vs2015_runtime-14.16 |  2.4 MB | ############################################################################## | 100%
Preparing transaction: done
Verifying transaction: done
```

### 1.2) Creating your Quant environment

Defining a specific environment for your Quantitative Analysis algorithms which will not clash with any previously defined environment.

```cmd
conda create --name quant python=3.8
```

```cmd
(base) C:\Users\thund>conda create --name quant python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\thund\Anaconda3\envs\quant

  added / updated specs:
    - python=3.8


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.6.24  |                0         125 KB
    certifi-2020.6.20          |           py38_0         157 KB
    openssl-1.1.1g             |       he774522_0         4.8 MB
    pip-20.1.1                 |           py38_1         1.7 MB
    python-3.8.3               |       he1778fa_2        15.6 MB
    setuptools-49.2.0          |           py38_0         752 KB
    sqlite-3.32.3              |       h2a8f88b_0         802 KB
    vs2015_runtime-14.16.27012 |       hf0eaf9b_3         1.2 MB
    wheel-0.34.2               |           py38_0          66 KB
    wincertstore-0.2           |           py38_0          15 KB
    zlib-1.2.11                |       h62dcd97_4         113 KB
    ------------------------------------------------------------
                                           Total:        25.3 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2020.6.24-0
  certifi            pkgs/main/win-64::certifi-2020.6.20-py38_0
  openssl            pkgs/main/win-64::openssl-1.1.1g-he774522_0
  pip                pkgs/main/win-64::pip-20.1.1-py38_1
  python             pkgs/main/win-64::python-3.8.3-he1778fa_2
  setuptools         pkgs/main/win-64::setuptools-49.2.0-py38_0
  sqlite             pkgs/main/win-64::sqlite-3.32.3-h2a8f88b_0
  vc                 pkgs/main/win-64::vc-14.1-h0510ff6_4
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.16.27012-hf0eaf9b_3
  wheel              pkgs/main/win-64::wheel-0.34.2-py38_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py38_0
  zlib               pkgs/main/win-64::zlib-1.2.11-h62dcd97_4


Proceed ([y]/n)? y


Downloading and Extracting Packages
openssl-1.1.1g       | 4.8 MB    | ############################################################################ | 100%
setuptools-49.2.0    | 752 KB    | ############################################################################ | 100%
sqlite-3.32.3        | 802 KB    | ############################################################################ | 100%
ca-certificates-2020 | 125 KB    | ############################################################################ | 100%
zlib-1.2.11          | 113 KB    | ############################################################################ | 100%
wincertstore-0.2     | 15 KB     | ############################################################################ | 100%
wheel-0.34.2         | 66 KB     | ############################################################################ | 100%
pip-20.1.1           | 1.7 MB    | ############################################################################ | 100%
python-3.8.3         | 15.6 MB   | ############################################################################ | 100%
vs2015_runtime-14.16 | 1.2 MB    | ############################################################################ | 100%
certifi-2020.6.20    | 157 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate quant
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

### 1.3) Activate your Quant environment

First we list our environments and then we enable the one we want

```cmd
(quant) C:\Users\thund>conda info --envs
# conda environments:
#
base                     C:\Users\thund\Anaconda3
quant                 *  C:\Users\thund\Anaconda3\envs\quant

(base) C:\Users\thund>conda activate quant

(quant) C:\Users\thund>
```

### 1.4) Install Spyder

Now we install the IDE using the command below:

```cmd
(quant) C:\Users\thund>conda install -c anaconda spyder
Collecting package metadata (current_repodata.json): done
Solving environment: |
Warning: 2 possible package resolutions (only showing differing packages):
  - anaconda/win-64::astroid-2.3.3-py38_0, anaconda/win-64::lazy-object-proxy-1.5.0-py38he774522_0, anaconda/win-64::pylint-2.4.4-py38_0, anaconda/win-64::wrapt-1.12.1-py38he774522_1
  - anaconda/win-64::astroid-2.4.2-py38_0, anaconda/win-64::lazy-object-proxy-1.4.3-py38he774522_0, anaconda/win-64::pylint-2.5.3-py38_0, anaconda/win-64::wrapt-1.11.2-py38he774522done

## Package Plan ##

  environment location: C:\Users\thund\Anaconda3\envs\quant

  added / updated specs:
    - spyder


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    alabaster-0.7.12           |             py_0          16 KB  anaconda
    argh-0.26.2                |           py38_0          37 KB  anaconda
    astroid-2.3.3              |           py38_0         290 KB  anaconda
    atomicwrites-1.4.0         |             py_0          11 KB  anaconda
    attrs-19.3.0               |             py_0          39 KB  anaconda
    autopep8-1.5.3             |             py_0          44 KB  anaconda
    babel-2.8.0                |             py_0         6.0 MB  anaconda
    backcall-0.2.0             |             py_0          14 KB  anaconda
    bcrypt-3.1.7               |   py38he774522_1          43 KB  anaconda
    bleach-3.1.5               |             py_0         116 KB  anaconda
    brotlipy-0.7.0             |py38he774522_1000         370 KB  anaconda
    ca-certificates-2020.6.24  |                0         165 KB  anaconda
    certifi-2020.6.20          |           py38_0         160 KB  anaconda
    cffi-1.14.0                |   py38h7a1dbc1_0         229 KB  anaconda
    chardet-3.0.4              |        py38_1003         190 KB  anaconda
    cloudpickle-1.5.0          |             py_0          22 KB  anaconda
    colorama-0.4.3             |             py_0          20 KB  anaconda
    cryptography-2.9.2         |   py38h7a1dbc1_0         590 KB  anaconda
    decorator-4.4.2            |             py_0          14 KB  anaconda
    defusedxml-0.6.0           |             py_0          23 KB  anaconda
    diff-match-patch-20200713  |             py_0          41 KB  anaconda
    docutils-0.16              |           py38_1         749 KB  anaconda
    entrypoints-0.3            |           py38_0          10 KB  anaconda
    flake8-3.8.3               |             py_0          96 KB  anaconda
    future-0.18.2              |           py38_1         746 KB  anaconda
    icu-58.2                   |   vc14hc45fdbb_0        21.9 MB  anaconda
    idna-2.10                  |             py_0          56 KB  anaconda
    imagesize-1.2.0            |             py_0          10 KB  anaconda
    importlib-metadata-1.7.0   |           py38_0          51 KB  anaconda
    importlib_metadata-1.7.0   |                0          11 KB  anaconda
    intervaltree-3.0.2         |             py_1          25 KB  anaconda
    ipykernel-5.3.2            |   py38h5ca1d4c_0         177 KB  anaconda
    ipython-7.16.1             |   py38h5ca1d4c_0         1.1 MB  anaconda
    ipython_genutils-0.2.0     |           py38_0          40 KB  anaconda
    isort-4.3.21               |           py38_0          83 KB  anaconda
    jedi-0.17.1                |           py38_0         950 KB  anaconda
    jinja2-2.11.2              |             py_0          97 KB  anaconda
    jpeg-9b                    |   vc14h4d7706e_1         313 KB  anaconda
    jsonschema-3.2.0           |           py38_0         112 KB  anaconda
    jupyter_client-6.1.6       |             py_0          83 KB  anaconda
    jupyter_core-4.6.3         |           py38_0          98 KB  anaconda
    keyring-21.2.1             |           py38_0          74 KB  anaconda
    lazy-object-proxy-1.5.0    |   py38he774522_0          34 KB  anaconda
    libpng-1.6.37              |       h2a8f88b_0         598 KB  anaconda
    libsodium-1.0.18           |       h62dcd97_0         666 KB  anaconda
    libspatialindex-1.9.3      |       h33f27b4_0         430 KB  anaconda
    markupsafe-1.1.1           |   py38he774522_0          30 KB  anaconda
    mccabe-0.6.1               |           py38_1          14 KB  anaconda
    mistune-0.8.4              |py38he774522_1000          54 KB  anaconda
    nbconvert-5.6.1            |           py38_0         505 KB  anaconda
    nbformat-5.0.7             |             py_0         103 KB  anaconda
    numpydoc-1.1.0             |             py_0          41 KB  anaconda
    openssl-1.1.1g             |       he774522_0         5.8 MB  anaconda
    packaging-20.4             |             py_0          35 KB  anaconda
    pandoc-2.10                |                0        29.5 MB  anaconda
    pandocfilters-1.4.2        |           py38_1          14 KB  anaconda
    paramiko-2.7.1             |             py_0         139 KB  anaconda
    parso-0.7.0                |             py_0          71 KB  anaconda
    pathtools-0.1.2            |             py_1          10 KB  anaconda
    pexpect-4.8.0              |           py38_0          84 KB  anaconda
    pickleshare-0.7.5          |        py38_1000          14 KB  anaconda
    pluggy-0.13.1              |           py38_0          33 KB  anaconda
    prompt-toolkit-3.0.5       |             py_0         240 KB  anaconda
    psutil-5.7.0               |   py38he774522_0         355 KB  anaconda
    pycodestyle-2.6.0          |             py_0          41 KB  anaconda
    pycparser-2.20             |             py_2          94 KB  anaconda
    pydocstyle-5.0.2           |             py_0          36 KB  anaconda
    pyflakes-2.2.0             |             py_0          59 KB  anaconda
    pygments-2.6.1             |             py_0         687 KB  anaconda
    pylint-2.4.4               |           py38_0         466 KB  anaconda
    pynacl-1.4.0               |   py38h62dcd97_0         1.5 MB  anaconda
    pyopenssl-19.1.0           |             py_1          47 KB  anaconda
    pyparsing-2.4.7            |             py_0          64 KB  anaconda
    pyqt-5.9.2                 |   py38ha925a31_4         4.1 MB  anaconda
    pyrsistent-0.16.0          |   py38he774522_0          96 KB  anaconda
    pysocks-1.7.1              |           py38_0          28 KB  anaconda
    python-dateutil-2.8.1      |             py_0         224 KB  anaconda
    python-jsonrpc-server-0.3.4|             py_1          11 KB  anaconda
    python-language-server-0.34.1|           py38_0          96 KB  anaconda
    pytz-2020.1                |             py_0         239 KB  anaconda
    pywin32-227                |   py38he774522_1         9.6 MB  anaconda
    pywin32-ctypes-0.2.0       |        py38_1000          40 KB  anaconda
    pyyaml-5.3.1               |   py38he774522_0         168 KB  anaconda
    pyzmq-19.0.1               |   py38ha925a31_1         495 KB  anaconda
    qdarkstyle-2.8.1           |             py_0         156 KB  anaconda
    qt-5.9.7                   |   vc14h73c81de_0        92.3 MB  anaconda
    qtawesome-0.7.2            |             py_0         807 KB  anaconda
    qtconsole-4.7.5            |             py_0          94 KB  anaconda
    qtpy-1.9.0                 |             py_0          39 KB  anaconda
    requests-2.24.0            |             py_0          54 KB  anaconda
    rope-0.17.0                |             py_0         120 KB  anaconda
    rtree-0.9.4                |   py38h21ff451_1          49 KB  anaconda
    sip-4.19.23                |   py38ha925a31_0         287 KB  anaconda
    six-1.15.0                 |             py_0          13 KB  anaconda
    snowballstemmer-2.0.0      |             py_0          58 KB  anaconda
    sortedcontainers-2.2.2     |             py_0          30 KB  anaconda
    sphinx-3.1.2               |             py_0         1.5 MB  anaconda
    sphinxcontrib-applehelp-1.0.2|             py_0          30 KB  anaconda
    sphinxcontrib-devhelp-1.0.2|             py_0          24 KB  anaconda
    sphinxcontrib-htmlhelp-1.0.3|             py_0          29 KB  anaconda
    sphinxcontrib-jsmath-1.0.1 |             py_0           8 KB  anaconda
    sphinxcontrib-qthelp-1.0.3 |             py_0          26 KB  anaconda
    sphinxcontrib-serializinghtml-1.1.4|             py_0          25 KB  anaconda
    spyder-4.1.4               |           py38_0         8.2 MB  anaconda
    spyder-kernels-1.9.2       |           py38_0          95 KB  anaconda
    testpath-0.4.4             |             py_0          88 KB  anaconda
    toml-0.10.1                |             py_0          20 KB  anaconda
    tornado-6.0.4              |   py38he774522_1         653 KB  anaconda
    traitlets-4.3.3            |           py38_0         135 KB  anaconda
    ujson-1.35                 |   py38he774522_0          27 KB  anaconda
    urllib3-1.25.9             |             py_0          98 KB  anaconda
    watchdog-0.10.3            |           py38_0         112 KB  anaconda
    wcwidth-0.2.5              |             py_0          37 KB  anaconda
    webencodings-0.5.1         |           py38_1          20 KB  anaconda
    win_inet_pton-1.1.0        |           py38_0           8 KB  anaconda
    wrapt-1.12.1               |   py38he774522_1          49 KB  anaconda
    yaml-0.1.7                 |   vc14h4cb57cf_1         103 KB  anaconda
    yapf-0.30.0                |             py_0         127 KB  anaconda
    zeromq-4.3.2               |       ha925a31_2         8.7 MB  anaconda
    zipp-3.1.0                 |             py_0          13 KB  anaconda
    ------------------------------------------------------------
                                           Total:       205.9 MB

The following NEW packages will be INSTALLED:

  alabaster          anaconda/noarch::alabaster-0.7.12-py_0
  argh               anaconda/win-64::argh-0.26.2-py38_0
  astroid            anaconda/win-64::astroid-2.3.3-py38_0
  atomicwrites       anaconda/noarch::atomicwrites-1.4.0-py_0
  attrs              anaconda/noarch::attrs-19.3.0-py_0
  autopep8           anaconda/noarch::autopep8-1.5.3-py_0
  babel              anaconda/noarch::babel-2.8.0-py_0
  backcall           anaconda/noarch::backcall-0.2.0-py_0
  bcrypt             anaconda/win-64::bcrypt-3.1.7-py38he774522_1
  bleach             anaconda/noarch::bleach-3.1.5-py_0
  brotlipy           anaconda/win-64::brotlipy-0.7.0-py38he774522_1000
  cffi               anaconda/win-64::cffi-1.14.0-py38h7a1dbc1_0
  chardet            anaconda/win-64::chardet-3.0.4-py38_1003
  cloudpickle        anaconda/noarch::cloudpickle-1.5.0-py_0
  colorama           anaconda/noarch::colorama-0.4.3-py_0
  cryptography       anaconda/win-64::cryptography-2.9.2-py38h7a1dbc1_0
  decorator          anaconda/noarch::decorator-4.4.2-py_0
  defusedxml         anaconda/noarch::defusedxml-0.6.0-py_0
  diff-match-patch   anaconda/noarch::diff-match-patch-20200713-py_0
  docutils           anaconda/win-64::docutils-0.16-py38_1
  entrypoints        anaconda/win-64::entrypoints-0.3-py38_0
  flake8             anaconda/noarch::flake8-3.8.3-py_0
  future             anaconda/win-64::future-0.18.2-py38_1
  icu                anaconda/win-64::icu-58.2-vc14hc45fdbb_0
  idna               anaconda/noarch::idna-2.10-py_0
  imagesize          anaconda/noarch::imagesize-1.2.0-py_0
  importlib-metadata anaconda/win-64::importlib-metadata-1.7.0-py38_0
  importlib_metadata anaconda/noarch::importlib_metadata-1.7.0-0
  intervaltree       anaconda/noarch::intervaltree-3.0.2-py_1
  ipykernel          anaconda/win-64::ipykernel-5.3.2-py38h5ca1d4c_0
  ipython            anaconda/win-64::ipython-7.16.1-py38h5ca1d4c_0
  ipython_genutils   anaconda/win-64::ipython_genutils-0.2.0-py38_0
  isort              anaconda/win-64::isort-4.3.21-py38_0
  jedi               anaconda/win-64::jedi-0.17.1-py38_0
  jinja2             anaconda/noarch::jinja2-2.11.2-py_0
  jpeg               anaconda/win-64::jpeg-9b-vc14h4d7706e_1
  jsonschema         anaconda/win-64::jsonschema-3.2.0-py38_0
  jupyter_client     anaconda/noarch::jupyter_client-6.1.6-py_0
  jupyter_core       anaconda/win-64::jupyter_core-4.6.3-py38_0
  keyring            anaconda/win-64::keyring-21.2.1-py38_0
  lazy-object-proxy  anaconda/win-64::lazy-object-proxy-1.5.0-py38he774522_0
  libpng             anaconda/win-64::libpng-1.6.37-h2a8f88b_0
  libsodium          anaconda/win-64::libsodium-1.0.18-h62dcd97_0
  libspatialindex    anaconda/win-64::libspatialindex-1.9.3-h33f27b4_0
  markupsafe         anaconda/win-64::markupsafe-1.1.1-py38he774522_0
  mccabe             anaconda/win-64::mccabe-0.6.1-py38_1
  mistune            anaconda/win-64::mistune-0.8.4-py38he774522_1000
  nbconvert          anaconda/win-64::nbconvert-5.6.1-py38_0
  nbformat           anaconda/noarch::nbformat-5.0.7-py_0
  numpydoc           anaconda/noarch::numpydoc-1.1.0-py_0
  packaging          anaconda/noarch::packaging-20.4-py_0
  pandoc             anaconda/win-64::pandoc-2.10-0
  pandocfilters      anaconda/win-64::pandocfilters-1.4.2-py38_1
  paramiko           anaconda/noarch::paramiko-2.7.1-py_0
  parso              anaconda/noarch::parso-0.7.0-py_0
  pathtools          anaconda/noarch::pathtools-0.1.2-py_1
  pexpect            anaconda/win-64::pexpect-4.8.0-py38_0
  pickleshare        anaconda/win-64::pickleshare-0.7.5-py38_1000
  pluggy             anaconda/win-64::pluggy-0.13.1-py38_0
  prompt-toolkit     anaconda/noarch::prompt-toolkit-3.0.5-py_0
  psutil             anaconda/win-64::psutil-5.7.0-py38he774522_0
  pycodestyle        anaconda/noarch::pycodestyle-2.6.0-py_0
  pycparser          anaconda/noarch::pycparser-2.20-py_2
  pydocstyle         anaconda/noarch::pydocstyle-5.0.2-py_0
  pyflakes           anaconda/noarch::pyflakes-2.2.0-py_0
  pygments           anaconda/noarch::pygments-2.6.1-py_0
  pylint             anaconda/win-64::pylint-2.4.4-py38_0
  pynacl             anaconda/win-64::pynacl-1.4.0-py38h62dcd97_0
  pyopenssl          anaconda/noarch::pyopenssl-19.1.0-py_1
  pyparsing          anaconda/noarch::pyparsing-2.4.7-py_0
  pyqt               anaconda/win-64::pyqt-5.9.2-py38ha925a31_4
  pyrsistent         anaconda/win-64::pyrsistent-0.16.0-py38he774522_0
  pysocks            anaconda/win-64::pysocks-1.7.1-py38_0
  python-dateutil    anaconda/noarch::python-dateutil-2.8.1-py_0
  python-jsonrpc-se~ anaconda/noarch::python-jsonrpc-server-0.3.4-py_1
  python-language-s~ anaconda/win-64::python-language-server-0.34.1-py38_0
  pytz               anaconda/noarch::pytz-2020.1-py_0
  pywin32            anaconda/win-64::pywin32-227-py38he774522_1
  pywin32-ctypes     anaconda/win-64::pywin32-ctypes-0.2.0-py38_1000
  pyyaml             anaconda/win-64::pyyaml-5.3.1-py38he774522_0
  pyzmq              anaconda/win-64::pyzmq-19.0.1-py38ha925a31_1
  qdarkstyle         anaconda/noarch::qdarkstyle-2.8.1-py_0
  qt                 anaconda/win-64::qt-5.9.7-vc14h73c81de_0
  qtawesome          anaconda/noarch::qtawesome-0.7.2-py_0
  qtconsole          anaconda/noarch::qtconsole-4.7.5-py_0
  qtpy               anaconda/noarch::qtpy-1.9.0-py_0
  requests           anaconda/noarch::requests-2.24.0-py_0
  rope               anaconda/noarch::rope-0.17.0-py_0
  rtree              anaconda/win-64::rtree-0.9.4-py38h21ff451_1
  sip                anaconda/win-64::sip-4.19.23-py38ha925a31_0
  six                anaconda/noarch::six-1.15.0-py_0
  snowballstemmer    anaconda/noarch::snowballstemmer-2.0.0-py_0
  sortedcontainers   anaconda/noarch::sortedcontainers-2.2.2-py_0
  sphinx             anaconda/noarch::sphinx-3.1.2-py_0
  sphinxcontrib-app~ anaconda/noarch::sphinxcontrib-applehelp-1.0.2-py_0
  sphinxcontrib-dev~ anaconda/noarch::sphinxcontrib-devhelp-1.0.2-py_0
  sphinxcontrib-htm~ anaconda/noarch::sphinxcontrib-htmlhelp-1.0.3-py_0
  sphinxcontrib-jsm~ anaconda/noarch::sphinxcontrib-jsmath-1.0.1-py_0
  sphinxcontrib-qth~ anaconda/noarch::sphinxcontrib-qthelp-1.0.3-py_0
  sphinxcontrib-ser~ anaconda/noarch::sphinxcontrib-serializinghtml-1.1.4-py_0
  spyder             anaconda/win-64::spyder-4.1.4-py38_0
  spyder-kernels     anaconda/win-64::spyder-kernels-1.9.2-py38_0
  testpath           anaconda/noarch::testpath-0.4.4-py_0
  toml               anaconda/noarch::toml-0.10.1-py_0
  tornado            anaconda/win-64::tornado-6.0.4-py38he774522_1
  traitlets          anaconda/win-64::traitlets-4.3.3-py38_0
  ujson              anaconda/win-64::ujson-1.35-py38he774522_0
  urllib3            anaconda/noarch::urllib3-1.25.9-py_0
  watchdog           anaconda/win-64::watchdog-0.10.3-py38_0
  wcwidth            anaconda/noarch::wcwidth-0.2.5-py_0
  webencodings       anaconda/win-64::webencodings-0.5.1-py38_1
  win_inet_pton      anaconda/win-64::win_inet_pton-1.1.0-py38_0
  wrapt              anaconda/win-64::wrapt-1.12.1-py38he774522_1
  yaml               anaconda/win-64::yaml-0.1.7-vc14h4cb57cf_1
  yapf               anaconda/noarch::yapf-0.30.0-py_0
  zeromq             anaconda/win-64::zeromq-4.3.2-ha925a31_2
  zipp               anaconda/noarch::zipp-3.1.0-py_0

The following packages will be SUPERSEDED by a higher-priority channel:

  ca-certificates                                 pkgs/main --> anaconda
  certifi                                         pkgs/main --> anaconda
  openssl                                         pkgs/main --> anaconda


Proceed ([y]/n)? y


Downloading and Extracting Packages
jsonschema-3.2.0     | 112 KB    | ############################################################################ | 100%
mccabe-0.6.1         | 14 KB     | ############################################################################ | 100%
sphinxcontrib-jsmath | 8 KB      | ############################################################################ | 100%
toml-0.10.1          | 20 KB     | ############################################################################ | 100%
imagesize-1.2.0      | 10 KB     | ############################################################################ | 100%
zeromq-4.3.2         | 8.7 MB    | ############################################################################ | 100%
importlib_metadata-1 | 11 KB     | ############################################################################ | 100%
six-1.15.0           | 13 KB     | ############################################################################ | 100%
bcrypt-3.1.7         | 43 KB     | ############################################################################ | 100%
urllib3-1.25.9       | 98 KB     | ############################################################################ | 100%
sphinx-3.1.2         | 1.5 MB    | ############################################################################ | 100%
pywin32-227          | 9.6 MB    | ############################################################################ | 100%
keyring-21.2.1       | 74 KB     | ############################################################################ | 100%
sip-4.19.23          | 287 KB    | ############################################################################ | 100%
spyder-4.1.4         | 8.2 MB    | ############################################################################ | 100%
intervaltree-3.0.2   | 25 KB     | ############################################################################ | 100%
argh-0.26.2          | 37 KB     | ############################################################################ | 100%
prompt-toolkit-3.0.5 | 240 KB    | ############################################################################ | 100%
ujson-1.35           | 27 KB     | ############################################################################ | 100%
jpeg-9b              | 313 KB    | ############################################################################ | 100%
jinja2-2.11.2        | 97 KB     | ############################################################################ | 100%
sphinxcontrib-serial | 25 KB     | ############################################################################ | 100%
nbconvert-5.6.1      | 505 KB    | ############################################################################ | 100%
jedi-0.17.1          | 950 KB    | ############################################################################ | 100%
icu-58.2             | 21.9 MB   | ############################################################################ | 100%
rope-0.17.0          | 120 KB    | ############################################################################ | 100%
win_inet_pton-1.1.0  | 8 KB      | ############################################################################ | 100%
jupyter_client-6.1.6 | 83 KB     | ############################################################################ | 100%
pydocstyle-5.0.2     | 36 KB     | ############################################################################ | 100%
libsodium-1.0.18     | 666 KB    | ############################################################################ | 100%
sphinxcontrib-qthelp | 26 KB     | ############################################################################ | 100%
pywin32-ctypes-0.2.0 | 40 KB     | ############################################################################ | 100%
ca-certificates-2020 | 165 KB    | ############################################################################ | 100%
python-dateutil-2.8. | 224 KB    | ############################################################################ | 100%
pysocks-1.7.1        | 28 KB     | ############################################################################ | 100%
packaging-20.4       | 35 KB     | ############################################################################ | 100%
colorama-0.4.3       | 20 KB     | ############################################################################ | 100%
wcwidth-0.2.5        | 37 KB     | ############################################################################ | 100%
atomicwrites-1.4.0   | 11 KB     | ############################################################################ | 100%
tornado-6.0.4        | 653 KB    | ############################################################################ | 100%
diff-match-patch-202 | 41 KB     | ############################################################################ | 100%
pyqt-5.9.2           | 4.1 MB    | ############################################################################ | 100%
nbformat-5.0.7       | 103 KB    | ############################################################################ | 100%
sphinxcontrib-devhel | 24 KB     | ############################################################################ | 100%
docutils-0.16        | 749 KB    | ############################################################################ | 100%
yapf-0.30.0          | 127 KB    | ############################################################################ | 100%
pycparser-2.20       | 94 KB     | ############################################################################ | 100%
bleach-3.1.5         | 116 KB    | ############################################################################ | 100%
babel-2.8.0          | 6.0 MB    | ############################################################################ | 100%
qt-5.9.7             | 92.3 MB   | ############################################################################ | 100%
pandocfilters-1.4.2  | 14 KB     | ############################################################################ | 100%
sphinxcontrib-htmlhe | 29 KB     | ############################################################################ | 100%
idna-2.10            | 56 KB     | ############################################################################ | 100%
ipykernel-5.3.2      | 177 KB    | ############################################################################ | 100%
snowballstemmer-2.0. | 58 KB     | ############################################################################ | 100%
libspatialindex-1.9. | 430 KB    | ############################################################################ | 100%
cffi-1.14.0          | 229 KB    | ############################################################################ | 100%
mistune-0.8.4        | 54 KB     | ############################################################################ | 100%
flake8-3.8.3         | 96 KB     | ############################################################################ | 100%
cloudpickle-1.5.0    | 22 KB     | ############################################################################ | 100%
backcall-0.2.0       | 14 KB     | ############################################################################ | 100%
zipp-3.1.0           | 13 KB     | ############################################################################ | 100%
brotlipy-0.7.0       | 370 KB    | ############################################################################ | 100%
parso-0.7.0          | 71 KB     | ############################################################################ | 100%
astroid-2.3.3        | 290 KB    | ############################################################################ | 100%
pyflakes-2.2.0       | 59 KB     | ############################################################################ | 100%
pyzmq-19.0.1         | 495 KB    | ############################################################################ | 100%
importlib-metadata-1 | 51 KB     | ############################################################################ | 100%
alabaster-0.7.12     | 16 KB     | ############################################################################ | 100%
isort-4.3.21         | 83 KB     | ############################################################################ | 100%
testpath-0.4.4       | 88 KB     | ############################################################################ | 100%
pyopenssl-19.1.0     | 47 KB     | ############################################################################ | 100%
qdarkstyle-2.8.1     | 156 KB    | ############################################################################ | 100%
pynacl-1.4.0         | 1.5 MB    | ############################################################################ | 100%
webencodings-0.5.1   | 20 KB     | ############################################################################ | 100%
ipython-7.16.1       | 1.1 MB    | ############################################################################ | 100%
qtconsole-4.7.5      | 94 KB     | ############################################################################ | 100%
decorator-4.4.2      | 14 KB     | ############################################################################ | 100%
pandoc-2.10          | 29.5 MB   | ############################################################################ | 100%
qtawesome-0.7.2      | 807 KB    | ############################################################################ | 100%
pexpect-4.8.0        | 84 KB     | ############################################################################ | 100%
jupyter_core-4.6.3   | 98 KB     | ############################################################################ | 100%
chardet-3.0.4        | 190 KB    | ############################################################################ | 100%
ipython_genutils-0.2 | 40 KB     | ############################################################################ | 100%
paramiko-2.7.1       | 139 KB    | ############################################################################ | 100%
future-0.18.2        | 746 KB    | ############################################################################ | 100%
pluggy-0.13.1        | 33 KB     | ############################################################################ | 100%
sortedcontainers-2.2 | 30 KB     | ############################################################################ | 100%
requests-2.24.0      | 54 KB     | ############################################################################ | 100%
rtree-0.9.4          | 49 KB     | ############################################################################ | 100%
qtpy-1.9.0           | 39 KB     | ############################################################################ | 100%
defusedxml-0.6.0     | 23 KB     | ############################################################################ | 100%
openssl-1.1.1g       | 5.8 MB    | ############################################################################ | 100%
wrapt-1.12.1         | 49 KB     | ############################################################################ | 100%
autopep8-1.5.3       | 44 KB     | ############################################################################ | 100%
numpydoc-1.1.0       | 41 KB     | ############################################################################ | 100%
psutil-5.7.0         | 355 KB    | ############################################################################ | 100%
sphinxcontrib-appleh | 30 KB     | ############################################################################ | 100%
cryptography-2.9.2   | 590 KB    | ############################################################################ | 100%
lazy-object-proxy-1. | 34 KB     | ############################################################################ | 100%
watchdog-0.10.3      | 112 KB    | ############################################################################ | 100%
libpng-1.6.37        | 598 KB    | ############################################################################ | 100%
pylint-2.4.4         | 466 KB    | ############################################################################ | 100%
pytz-2020.1          | 239 KB    | ############################################################################ | 100%
certifi-2020.6.20    | 160 KB    | ############################################################################ | 100%
yaml-0.1.7           | 103 KB    | ############################################################################ | 100%
pyrsistent-0.16.0    | 96 KB     | ############################################################################ | 100%
markupsafe-1.1.1     | 30 KB     | ############################################################################ | 100%
pyyaml-5.3.1         | 168 KB    | ############################################################################ | 100%
pyparsing-2.4.7      | 64 KB     | ############################################################################ | 100%
python-jsonrpc-serve | 11 KB     | ############################################################################ | 100%
python-language-serv | 96 KB     | ############################################################################ | 100%
pickleshare-0.7.5    | 14 KB     | ############################################################################ | 100%
traitlets-4.3.3      | 135 KB    | ############################################################################ | 100%
pycodestyle-2.6.0    | 41 KB     | ############################################################################ | 100%
entrypoints-0.3      | 10 KB     | ############################################################################ | 100%
pygments-2.6.1       | 687 KB    | ############################################################################ | 100%
pathtools-0.1.2      | 10 KB     | ############################################################################ | 100%
spyder-kernels-1.9.2 | 95 KB     | ############################################################################ | 100%
attrs-19.3.0         | 39 KB     | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: \ DEBUG menuinst_win32:__init__(199): Menu: name: 'Anaconda${PY_VER} ${PLATFORM}', prefix: 'C:\Users\thund\Anaconda3\envs\quant', env_name: 'quant', mode: 'user', used_mode: 'user'
DEBUG menuinst_win32:create(323): Shortcut cmd is C:\Users\thund\Anaconda3\pythonw.exe, args are ['C:\\Users\\thund\\Anaconda3\\cwp.py', 'C:\\Users\\thund\\Anaconda3\\envs\\quant', 'C:\\Users\\thund\\Anaconda3\\envs\\quant\\pythonw.exe', 'C:\\Users\\thund\\Anaconda3\\envs\\quant\\Scripts\\spyder-script.py']
| DEBUG menuinst_win32:create(323): Shortcut cmd is C:\Users\thund\Anaconda3\python.exe, args are ['C:\\Users\\thund\\Anaconda3\\cwp.py', 'C:\\Users\\thund\\Anaconda3\\envs\\quant', 'C:\\Users\\thund\\Anaconda3\\envs\\quant\\python.exe', 'C:\\Users\\thund\\Anaconda3\\envs\\quant\\Scripts\\spyder-script.py', '--reset']
done
```
To launch spyder
```cmd
//launch
spyder
//launch new instance if there is one already there
spyder --new-instance
```

# 2) Downloading Stock Data using yFinance (Yahoo Finance)

We will use the implementation in one of my [repos](https://github.com/JordiCorbilla/stock-prediction-deep-neural-learning) that uses [yFinance](https://aroussi.com/post/python-yahoo-finance) library.

install yFinance using pip:

```cmd
(quant) C:\Users\thund>pip install yfinance --upgrade --no-cache-dir
Collecting yfinance
  Downloading yfinance-0.1.54.tar.gz (19 kB)
Collecting pandas>=0.24
  Downloading pandas-1.0.5-cp38-cp38-win_amd64.whl (8.9 MB)
     |████████████████████████████████| 8.9 MB 1.1 MB/s
Collecting numpy>=1.15
  Downloading numpy-1.19.0-cp38-cp38-win_amd64.whl (13.0 MB)
     |████████████████████████████████| 13.0 MB 3.3 MB/s
Requirement already satisfied, skipping upgrade: requests>=2.20 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from yfinance) (2.24.0)
Collecting multitasking>=0.0.7
  Downloading multitasking-0.0.9.tar.gz (8.1 kB)
Requirement already satisfied, skipping upgrade: python-dateutil>=2.6.1 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from pandas>=0.24->yfinance) (2.8.1)
Requirement already satisfied, skipping upgrade: pytz>=2017.2 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from pandas>=0.24->yfinance) (2020.1)
Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from requests>=2.20->yfinance) (2020.6.20)
Requirement already satisfied, skipping upgrade: chardet<4,>=3.0.2 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from requests>=2.20->yfinance) (3.0.4)
Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from requests>=2.20->yfinance) (1.25.9)
Requirement already satisfied, skipping upgrade: idna<3,>=2.5 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from requests>=2.20->yfinance) (2.10)
Requirement already satisfied, skipping upgrade: six>=1.5 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from python-dateutil>=2.6.1->pandas>=0.24->yfinance) (1.15.0)
Building wheels for collected packages: yfinance, multitasking
  Building wheel for yfinance (setup.py) ... done
  Created wheel for yfinance: filename=yfinance-0.1.54-py2.py3-none-any.whl size=22415 sha256=f2012024154c9d90ef74531a2d4d6ef612938ef0e5010d893af3f8b0e71f0b9b
  Stored in directory: C:\Users\thund\AppData\Local\Temp\pip-ephem-wheel-cache-3wmlyd71\wheels\d9\55\e4\3fc43a4f56c7c18628bc24088be1d7168a832a91efa5ccc5da
  Building wheel for multitasking (setup.py) ... done
  Created wheel for multitasking: filename=multitasking-0.0.9-py3-none-any.whl size=8374 sha256=9bb92d3d62a3ef2727bde33c8d52f06bc27e2acdeab301d89f9ec6c5bf95d8cd
  Stored in directory: C:\Users\thund\AppData\Local\Temp\pip-ephem-wheel-cache-3wmlyd71\wheels\57\6d\a3\a39b839cc75274d2acfb1c58bfead2f726c6577fe8c4723f13
Successfully built yfinance multitasking
Installing collected packages: numpy, pandas, multitasking, yfinance
Successfully installed multitasking-0.0.9 numpy-1.19.0 pandas-1.0.5 yfinance-0.1.54
```

# 2.1) Testing yFinance

