# PMCDSTI

This repository is a **public preview** of PMCDSTI, a conditional diffusion model for spatiotemporal data imputation.



## What Is Included

```text
PMCDSTI/
├── config/                 # Example YAML configuration files
├── datasets/               # Dataset loader interface placeholders
├── models/                 # Public PMCDSTI class interface placeholder
├── docs/                   # Release notes and checklist
├── requirements.txt
└── README.md
```



## Public Interface

The model interface is represented by:

```python
from models import PMCDSTI
```

Dataset loader placeholders are provided under `datasets/` to show expected file organization.

## Environment

A minimal dependency list is provided in `requirements.txt`. The final reproducible release may include additional environment details and version-pinned instructions.

## Data

Raw datasets are not included. Public datasets should be downloaded from their official sources. 

