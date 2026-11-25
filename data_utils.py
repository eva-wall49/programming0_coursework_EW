from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_data(filename, header_lines=7):
    """
    Return the rows of a Met Office station file as lists of strings.

    Provided for you - do not change. The file is read from the data folder
    next to this script, so it works wherever the script is run from. The
    header lines are skipped, and every remaining non-blank line is split on
    whitespace into a list of strings.
    """
    rows = []
    with open(DATA_DIR / filename) as f:
        for i, line in enumerate(f):
            if i >= header_lines and line.strip():
                rows.append(line.split())
    return rows
