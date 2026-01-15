# penr-oz-quantum-dwave-leap-api-example

Implementation of an example use of the D-Wave Leap Quantum Computing API.

## Repository layout

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   └── dwave.conf.example
├── src/
│   ├── __init__.py
│   ├── solvers.py
│   └── sample_problem.py
└── scripts/
    └── run_example.sh
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Export your Leap API token:

```bash
export DWAVE_API_TOKEN="your-token-here"
```

Alternatively, copy `config/dwave.conf.example` to `~/.config/dwave/dwave.conf` and
fill in your token.

## Run the example

```bash
python src/sample_problem.py
```

Or use the helper script:

```bash
scripts/run_example.sh
```

Optional flags:

```bash
python src/sample_problem.py --solver "Advantage_system6.1" --num-reads 200
```
