# mss-stubs

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/mss-stubs?style=flat)](https://pypi.org/project/mss-stubs/)

[PEP 561](https://peps.python.org/pep-0561/) type stubs for [mss](https://github.com/ScreenPy/mss), the cross-platform screenshot library.

`mss` ships without type annotations. Running Pyright or Pylance in strict mode will flag every `mss` call as unknown. This package fixes that.

---

## Install

```bash
pip install mss-stubs
```

Or with `uv`:

```bash
uv pip install mss-stubs
```

---

## Usage

Install alongside `mss` and your type checker picks it up automatically. No configuration needed.

```python
import mss

with mss.MSS() as sct:
    monitor = sct.monitors[1]   # dict[str, int]
    shot = sct.grab(monitor)    # ScreenShot
    print(shot.size)            # tuple[int, int]
    print(len(shot.bgra))       # bytes
```

---

## Covered API

| Symbol | Type |
|---|---|
| `mss.MSS()` | `MSSBase` |
| `MSSBase.monitors` | `list[dict[str, int]]` |
| `MSSBase.grab(monitor)` | `ScreenShot` |
| `MSSBase.__enter__` / `__exit__` | context manager |
| `ScreenShot.size` | `tuple[int, int]` |
| `ScreenShot.bgra` | `bytes` |

---

## License

Apache 2.0. See [LICENSE](LICENSE).  
&copy; 2026 [paredez.dev](https://paredez.dev)
