from classes import Child, Father, Mother
import sys

# tries to import colorama from ENV.
try:
    import colorama
except ImportError:
    print("Failed to import colorama. Check if installed in ENV.")
    print("pip install colorama")
    sys.exit(1)
