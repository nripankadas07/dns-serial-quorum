# dns-serial-quorum

Classify equal, ahead, behind, half-range ambiguous and unavailable observations; calculate an explicit equality quorum.

For dns operators reviewing a zone rollout across authoritative servers. Ordinary numeric comparison mishandles SOA serial rollover, while a partial rollout can look complete.

## Quickstart

Python 3.10 or newer. No runtime dependencies or service account. Build tooling downloads require access to PyPI; this repository is not published on PyPI.

```bash
git clone https://github.com/nripankadas07/dns-serial-quorum.git
cd dns-serial-quorum
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/dns-serial-quorum example.json
```

Windows: use `.venv\Scripts\python.exe` and `.venv\Scripts\dns-serial-quorum.exe` instead. Windows is not part of the tested CI matrix.

The supplied example is synthetic. JSON success exits 0, including valid findings such as unmet quorum, ineligible cookie or an ordering cycle; malformed or unsupported input exits 2 with an `error` field. Argument usage errors use argparse's stderr. No input files or live services are modified.

## Scope and limits

No live DNS queries, DNSSEC verification, TTL or propagation-time inference. Input is a single manually supplied authoritative-server snapshot. Server labels are asserted unique, not verified identities. RFC 1982 half-range ordering is undefined; ahead does not count as expected equality.

Input limits: 256 KiB JSON; 1..1,000 observations; unsigned 32-bit integer serials; null denotes unavailable.

## Inspectable evidence

- [Demo and input schema](DEMO.md)
- [Candidate brief and comparisons](RESEARCH.md)
- [Validation and untested behavior](VALIDATION.md)
- [Build instructions](BUILDING.md)
- [Security reporting](SECURITY.md) and [support/contribution guidance](SUPPORT.md)

MIT; original implementation. No competitor code or branding copied. No speed, adoption or superiority claim. CI executes core regressions, the demo, a fresh wheel installation outside source and the documented source installation on Python 3.10, 3.12 and 3.14.
