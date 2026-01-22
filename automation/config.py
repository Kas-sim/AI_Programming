from pathlib import Path

BASE = None

CATEGORIES = {
    "PDFs": {
        "folder": BASE / "PDFs",
        "ext": {".pdf"},
        "count": 0
    },
    "Office files": {
        "folder": BASE / "Office files",
        "ext": {".docx", ".xlsx", ".pptx", ".accdb"},
        "count": 0
    },
    "Text files": {
        "folder": BASE / "Text files",
        "ext": {".csv", ".json", ".txt", ".md"},
        "count": 0
    },
    "Images": {
        "folder": BASE / "Images",
        "ext": {".png", ".jpg", ".jpeg", ".ico"},
        "count": 0
    },
    "Videos": {
        "folder": BASE / "Videos",
        "ext": {".mp4", ".mov", ".mkv", ".avi"},
        "count": 0
    },
    "Audio files": {
        "folder": BASE / "Audio files",
        "ext": {".mp3", ".wav", ".m4a", ".aac"},
        "count": 0
    },
    "Coding Files": {
        "folder": BASE / "Coding Files",
        "ext": {".py", ".ipynb", ".java", ".html", ".cpp"},
        "count": 0
    },
    "Setups": {
        "folder": BASE / "Setups",
        "ext": {".exe"},
        "count": 0
    }
}
