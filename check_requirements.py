import importlib
import sys

REQUIRED_PACKAGES = [
    'flask',
    'flask_sqlalchemy',
    'flask_login',
    'flask_migrate',
    'yfinance',
    'pandas',
    'numpy',
    'requests',
    'lxml',
]

missing = []
for pkg in REQUIRED_PACKAGES:
    try:
        importlib.import_module(pkg)
    except ImportError:
        missing.append(pkg)

if missing:
    print("\nMissing required packages:")
    for pkg in missing:
        print(f"  - {pkg}")
    print("\nInstall them with:")
    print(f"  pip install {' '.join(missing)}")
    sys.exit(1)
else:
    print("All required packages are installed.") 