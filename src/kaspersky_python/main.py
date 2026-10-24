from .configs.env import read_env
from .console import Console
import os

def main() -> None:
    read_env()
    console = Console()
    console.run()

if __name__ == "__main__":
    main()