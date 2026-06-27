# General Knowledge Quiz — DecodeLabs Project 4
**Python Industrial Training Kit · Batch 2026**

---

## Setup & Run

```bash
pip install -r requirements.txt
python app.py
# → http://127.0.0.1:5000
```

---

## Project Structure

```
quiz_app/
├── app.py                ← Backend logic (control flow, score vault, sanitization)
├── requirements.txt
├── templates/
│   ├── index.html        ← Landing page (INPUT phase)
│   ├── quiz.html         ← Question page (INPUT phase)
│   ├── feedback.html     ← Per-question feedback (OUTPUT phase)
│   └── results.html      ← Final score breakdown (STORAGE phase)
└── static/
    └── style.css
```

---

## Quality Standard Checklist (Above the API Standard)

- [x] **Logic Consistency** — if/else paths fully mapped, no silent gaps
- [x] **Whitespace Audit** — `.strip()` applied on every answer capture
- [x] **Data Normalization** — `.lower()` applied uniformly to all inputs
- [x] **Type Integrity** — `score = 0` (integer), never overwritten as string
- [x] **Output Clarity** — `f"Score: {score}/{total}"` used throughout

---

## Key Concepts

| Concept | Code | DecodeLabs Term |
|---|---|---|
| Control Flow | `if correct: score += 1 / else: pass` | Logic Gate |
| Score Vault | `score = 0` (outside loop) | Anatomy of State |
| Input Sanitization | `.strip().lower()` | The Pro Recipe |
| f-string Output | `f"Score: {score}/{total}"` | F-String Injector |
| IPOS Architecture | Routes map to phases | Decision Engine Blueprint |

---

## Stretch Challenges

1. Add **10+ questions** loaded from a JSON file
2. Add a **timer** per question (countdown)
3. Add **difficulty levels** (Easy / Medium / Hard)
4. Store high scores in a **SQLite database**
