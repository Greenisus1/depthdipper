# Depthdipper

Strict JSON nesting-depth and type totals, no values/keys.

Python 3 standard library; offline terminal.

Run: `python3 depthdipper.py`

Tests: `python3 -m unittest -v`

App Store hooks: `bash app-store.sh install`, `bash app-store.sh run`. Version 1.0.0.

Regular strict UTF-8 JSON <=1 MiB, no BOM; duplicate keys/nonstandard constants rejected, numeric tokens avoid overflow. Root value depth 0, child value +1. Object keys not counted; empty containers each one value. Types and total/max depth only, source values/keys hidden; structure sensitive. Parser nesting limits apply; no schema/security checks, writes/network.

Linux tested; Pi/non-Linux untested.

The current public-only Pi App Store cannot discover private repositories; authenticated store support is not verified.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
