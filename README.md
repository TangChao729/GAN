## Getting Started

### Option 1: Using uv (Recommended - faster)
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone <your-repo-url>
cd GAN

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .

# Install dev dependencies (optional)
uv pip install -e ".[dev]"
```

### Option 2: Using pip
```bash
pip install -e .
```

## Repository Structure

```
GAN/
├── README.md
├── pyproject.toml          # Modern dependency management
├── .gitignore
├── src/
│   └── gan_learning/       # Main package
├── experiments/            # Experimental code and scripts
└── notebooks/              # Jupyter notebooks for exploration
```

## Development Approach

This project follows an iterative development approach with frequent commits and branching to track the evolution of the codebase from simple to professional level.
