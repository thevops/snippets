# Docker


Install with apt-get
```dockerfile
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
    curl \
    # other packages \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
```
