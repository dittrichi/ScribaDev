"""ScribaDev — gravação e transcrição automática de reuniões do Microsoft Teams."""

__version__ = "1.4.14"

# Instalação congelada (#142/#147): deps pesadas baixadas pelo wizard moram em
# APP_DIR/addons e precisam entrar no sys.path ANTES de qualquer import lazy
# (torch/pyannote/nvidia). Guardado por sys.frozen: no código-fonte é no-op puro.
import os as _os
import sys as _sys

_os.environ["PYTHONUTF8"] = "1"

if getattr(_sys, "frozen", False):
    from . import addons as _addons

    _addons.bootstrap()
