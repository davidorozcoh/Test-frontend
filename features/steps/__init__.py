import os
import importlib
import pkgutil

__all__ = []
PATH = os.path.dirname(__file__)

for loader, module_name, is_pkg in pkgutil.walk_packages([PATH]):
    try:
        # Carga del módulo usando importlib (más moderno y robusto)
        _module = importlib.import_module(f"{__name__}.{module_name}")
        globals()[module_name] = _module
        __all__.append(module_name)
    except Exception as e:
        print(f"Error loading module {module_name}: {e}")
