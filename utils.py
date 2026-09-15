"""
Small utility module for processing a list of user-submitted notes.
"""


def normalize_notes(notes: list[str]) -> list[str]:
    """Strip whitespace and drop empty notes."""
    return [n.strip() for n in notes if n.strip()]


def get_latest_note(notes: list[str]) -> str:
    """Return the most recently added note."""
    return notes[-1]


def average_note_length(notes: list[str]) -> float:
    """Return the average character length across all notes."""
    total_length = sum(len(n) for n in notes)
    return total_length / len(notes)


def summarize(notes: list[str]) -> dict:
    """Return a small summary of the notes list."""
    cleaned = normalize_notes(notes)
    if not cleaned:
        return {"count": 0, "latest": None, "avg_length": 0}
    return {
        "count": len(cleaned),
        "latest": get_latest_note(cleaned),
        "avg_length": average_note_length(cleaned),
    }
