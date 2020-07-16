# Quantitative Analysis

Algorithmic trading and Quantitative Analysis

## Setup
To execute all the code in this repo, we'll use [Anaconda3](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe) and [Spyder IDE](https://www.spyder-ide.org/) which will allow us to create virtual environments. Below is the list of packages to install and commands to run on the Anaconda console: 

### Updating Anaconda

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

### Creating your Quant environment

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

### Activate your Quant environment

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
