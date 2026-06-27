import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "quiz-decodelabs-project4-2026"

# ---------- HOW MANY QUESTIONS PER GAME ----------
QUESTIONS_PER_GAME = 10   # drawn randomly from the full bank each session

QUESTION_BANK = [
    # ── GEOGRAPHY (8) ────────────────────────────────────────
    {
        "id": 1,
        "question": "What is the capital of France?",
        "answers": ["paris"],
        "hint": "The city of lights, home of the Eiffel Tower.",
        "category": "Geography",
    },
    {
        "id": 2,
        "question": "How many continents are there on Earth?",
        "answers": ["7", "seven"],
        "hint": "Africa, Antarctica, Asia, Australia, Europe, North America, South America.",
        "category": "Geography",
    },
    {
        "id": 3,
        "question": "What is the longest river in the world?",
        "answers": ["nile", "nile river"],
        "hint": "It flows through Egypt and empties into the Mediterranean Sea.",
        "category": "Geography",
    },
    {
        "id": 4,
        "question": "Which country is the largest by land area?",
        "answers": ["russia"],
        "hint": "It spans 11 time zones across Eastern Europe and Northern Asia.",
        "category": "Geography",
    },
    {
        "id": 5,
        "question": "What is the capital of Japan?",
        "answers": ["tokyo"],
        "hint": "The most populous metropolitan area in the world.",
        "category": "Geography",
    },
    {
        "id": 6,
        "question": "Which ocean is the largest on Earth?",
        "answers": ["pacific", "pacific ocean"],
        "hint": "It covers more than 30% of Earth's surface.",
        "category": "Geography",
    },
    {
        "id": 7,
        "question": "In which country is the Amazon rainforest primarily located?",
        "answers": ["brazil"],
        "hint": "This South American country also hosts the 2016 Olympics.",
        "category": "Geography",
    },
    {
        "id": 8,
        "question": "What is the smallest country in the world?",
        "answers": ["vatican", "vatican city"],
        "hint": "It is an independent city-state located within Rome, Italy.",
        "category": "Geography",
    },

    # ── SCIENCE (8) ──────────────────────────────────────────
    {
        "id": 9,
        "question": "What is the largest planet in our Solar System?",
        "answers": ["jupiter"],
        "hint": "It has a famous Great Red Spot storm.",
        "category": "Science",
    },
    {
        "id": 10,
        "question": "What is the chemical symbol for water?",
        "answers": ["h2o"],
        "hint": "Two hydrogen atoms bonded to one oxygen atom.",
        "category": "Science",
    },
    {
        "id": 11,
        "question": "How many bones are in the adult human body?",
        "answers": ["206"],
        "hint": "Babies are born with around 270-300, many fuse over time.",
        "category": "Science",
    },
    {
        "id": 12,
        "question": "What planet is known as the Red Planet?",
        "answers": ["mars"],
        "hint": "NASA's Perseverance rover is currently exploring it.",
        "category": "Science",
    },
    {
        "id": 13,
        "question": "What is the powerhouse of the cell?",
        "answers": ["mitochondria", "the mitochondria"],
        "hint": "It produces ATP — the cell's energy currency.",
        "category": "Science",
    },
    {
        "id": 14,
        "question": "What gas do plants absorb during photosynthesis?",
        "answers": ["carbon dioxide", "co2"],
        "hint": "It is also the main greenhouse gas causing climate change.",
        "category": "Science",
    },
    {
        "id": 15,
        "question": "What is the speed of light in a vacuum (approximately)?",
        "answers": ["300000 km/s", "3x10^8 m/s", "299792 km/s", "300,000 km/s"],
        "hint": "It is approximately 3 × 10⁸ metres per second.",
        "category": "Science",
    },
    {
        "id": 16,
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "answers": ["nitrogen", "n2"],
        "hint": "It makes up about 78% of the air we breathe.",
        "category": "Science",
    },

    # ── LITERATURE & HISTORY (7) ─────────────────────────────
    {
        "id": 17,
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "answers": ["william shakespeare", "shakespeare"],
        "hint": "An English playwright from the 16th century.",
        "category": "Literature",
    },
    {
        "id": 18,
        "question": "Who wrote '1984'?",
        "answers": ["george orwell", "orwell"],
        "hint": "His real name was Eric Arthur Blair.",
        "category": "Literature",
    },
    {
        "id": 19,
        "question": "In which year did World War II end?",
        "answers": ["1945"],
        "hint": "V-E Day was May 8th and V-J Day was September 2nd of this year.",
        "category": "History",
    },
    {
        "id": 20,
        "question": "Who was the first President of the United States?",
        "answers": ["george washington", "washington"],
        "hint": "His face appears on the US one-dollar bill.",
        "category": "History",
    },
    {
        "id": 21,
        "question": "Who painted the Mona Lisa?",
        "answers": ["leonardo da vinci", "da vinci", "leonardo"],
        "hint": "He was also a scientist and inventor during the Italian Renaissance.",
        "category": "History",
    },
    {
        "id": 22,
        "question": "In which year did the Titanic sink?",
        "answers": ["1912"],
        "hint": "The ship hit an iceberg on April 14th of this year.",
        "category": "History",
    },
    {
        "id": 23,
        "question": "What ancient wonder was located in Alexandria, Egypt?",
        "answers": ["lighthouse", "lighthouse of alexandria", "pharos"],
        "hint": "It was one of the tallest man-made structures for centuries.",
        "category": "History",
    },

    # ── TECHNOLOGY & PYTHON (7) ──────────────────────────────
    {
        "id": 24,
        "question": "What programming language is this quiz built with?",
        "answers": ["python"],
        "hint": "Created by Guido van Rossum and named after a comedy show.",
        "category": "Technology",
    },
    {
        "id": 25,
        "question": "What does 'HTTP' stand for?",
        "answers": ["hypertext transfer protocol"],
        "hint": "It is the foundation of data communication on the World Wide Web.",
        "category": "Technology",
    },
    {
        "id": 26,
        "question": "What Python method removes leading and trailing whitespace from a string?",
        "answers": ["strip", ".strip", ".strip()", "strip()"],
        "hint": "It is the Whitespace Bouncer from your training kit.",
        "category": "Technology",
    },
    {
        "id": 27,
        "question": "What does 'CPU' stand for?",
        "answers": ["central processing unit"],
        "hint": "Often called the 'brain' of a computer.",
        "category": "Technology",
    },
    {
        "id": 28,
        "question": "In Python, what keyword is used to define a function?",
        "answers": ["def"],
        "hint": "Short for 'define'. It is followed by the function name.",
        "category": "Technology",
    },
    {
        "id": 29,
        "question": "What Flask function redirects the user to a different route?",
        "answers": ["redirect", "redirect()", "redirect(url_for(...))"],
        "hint": "It is imported from flask and often paired with url_for().",
        "category": "Technology",
    },
    {
        "id": 30,
        "question": "What data structure uses key-value pairs in Python?",
        "answers": ["dictionary", "dict"],
        "hint": "It uses curly braces {} and colons to map keys to values.",
        "category": "Technology",
    },
]


# ---------- HELPER FUNCTIONS ----------

def evaluate_answer(user_input: str, valid_answers: list) -> bool:
    """
    The Question Block Process Phase — The Pro Recipe.
    .strip()  → Whitespace Bouncer: removes accidental spaces/tabs/newlines
    .lower()  → Neutralizer: case-insensitive comparison
    in        → checks against all accepted aliases
    """
    sanitized = user_input.strip().lower()
    return sanitized in valid_answers


def score_label(score: int, total: int) -> tuple:
    """Return (label, css_class) based on percentage score."""
    pct = (score / total) * 100
    if pct == 100:
        return ("Perfect Score! 🏆", "perfect")
    elif pct >= 80:
        return ("Excellent! ⭐", "excellent")
    elif pct >= 60:
        return ("Good Job! 👍", "good")
    elif pct >= 40:
        return ("Keep Practicing! 📚", "average")
    else:
        return ("Better Luck Next Time! 💪", "low")


def get_session_questions():
    """
    NON-REPEATING QUESTION SELECTION — random.sample()
    ─────────────────────────────────────────────────────
    random.sample(population, k) returns k UNIQUE items
    from population WITHOUT replacement — no repeats guaranteed.

    The selected question IDs are stored in session["q_ids"],
    so every GET /quiz simply looks up the next ID in that list.
    No question can appear twice in a single playthrough.

    On the NEXT game (hitting /), session.clear() runs and a
    brand-new sample is drawn → different question set every game.
    """
    selected = random.sample(QUESTION_BANK, QUESTIONS_PER_GAME)
    return selected


# ---------- ROUTES ----------

@app.route("/")
def index():
    """Landing page — start or restart the quiz. Clears all session state."""
    session.clear()
    return render_template("index.html",
                           total=QUESTIONS_PER_GAME,
                           bank_size=len(QUESTION_BANK))


@app.route("/quiz", methods=["GET"])
def quiz():
    """
    IPOS Architecture — INPUT phase.
    On first visit: draw a fresh random sample via random.sample(),
    store question IDs in session. Never repeats within a session.
    """
    # ── First visit: initialize session state ──
    if "q_ids" not in session:
        selected = get_session_questions()
        # Store only IDs (lightweight) — we look up full question by ID at render time
        session["q_ids"]   = [q["id"] for q in selected]
        session["q_index"] = 0
        session["score"]   = 0      # SCORE VAULT — integer, initialized once
        session["results"] = []

    q_index = session["q_index"]
    total   = len(session["q_ids"])

    # All questions answered → go to results
    if q_index >= total:
        return redirect(url_for("results"))

    # Look up the current question by ID from our session's ordered list
    current_id = session["q_ids"][q_index]
    current_q  = next(q for q in QUESTION_BANK if q["id"] == current_id)
    progress_pct = int((q_index / total) * 100)

    return render_template("quiz.html",
                           question=current_q,
                           q_num=q_index + 1,
                           total=total,
                           score=session["score"],
                           progress_pct=progress_pct)


@app.route("/quiz", methods=["POST"])
def submit_answer():
    """
    IPOS Architecture — PROCESS + STORAGE phase.
    Sanitize → Evaluate → score += 1 if correct → store result.
    """
    q_index   = session.get("q_index", 0)
    raw_ans   = request.form.get("answer", "")
    total     = len(session.get("q_ids", []))

    # Guard: session expired mid-quiz
    if not session.get("q_ids") or q_index >= total:
        return redirect(url_for("index"))

    current_id = session["q_ids"][q_index]
    current_q  = next(q for q in QUESTION_BANK if q["id"] == current_id)

    # CONTROL FLOW — The Logic Gate
    is_correct = evaluate_answer(raw_ans, current_q["answers"])

    if is_correct:
        session["score"] = session["score"] + 1   # integer accumulator
        feedback = "correct"
    else:
        feedback = "incorrect"                     # score sustained, not reset

    # STORAGE — append result for the breakdown page
    results = session.get("results", [])
    results.append({
        "question":      current_q["question"],
        "category":      current_q["category"],
        "user_answer":   raw_ans.strip(),
        "correct_answer": current_q["answers"][0].title(),
        "is_correct":    is_correct,
        "feedback":      feedback,
    })
    session["results"]  = results
    session["q_index"]  = q_index + 1
    session.modified    = True

    return redirect(url_for("feedback",
                            correct=int(is_correct),
                            q_index=q_index))


@app.route("/feedback")
def feedback():
    """
    IPOS Architecture — OUTPUT phase.
    Per-question feedback with sanitization pipeline shown live.
    """
    is_correct = bool(int(request.args.get("correct", 0)))
    q_index    = int(request.args.get("q_index", 0))
    total      = len(session.get("q_ids", [QUESTIONS_PER_GAME]))

    current_id = session["q_ids"][q_index]
    current_q  = next(q for q in QUESTION_BANK if q["id"] == current_id)

    score    = session.get("score", 0)
    user_ans = session["results"][-1]["user_answer"] if session.get("results") else ""

    return render_template("feedback.html",
                           is_correct=is_correct,
                           question=current_q,
                           user_answer=user_ans,
                           score=score,
                           q_num=q_index + 1,
                           total=total,
                           more=session.get("q_index", 0) < total)


@app.route("/results")
def results():
    """
    IPOS Architecture — OUTPUT phase (final).
    Final score with f-string display and full per-question breakdown.
    """
    score   = session.get("score", 0)
    total   = len(session.get("q_ids", [QUESTIONS_PER_GAME]))
    results = session.get("results", [])
    label, css = score_label(score, total)
    score_display = f"{score} / {total}"      # f-string Output Clarity standard

    return render_template("results.html",
                           score=score,
                           total=total,
                           score_display=score_display,
                           label=label,
                           css=css,
                           results=results,
                           bank_size=len(QUESTION_BANK))


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    print(f"\n  🧠 Quiz running — {len(QUESTION_BANK)} questions in bank,")
    print(f"     {QUESTIONS_PER_GAME} drawn per game via random.sample()")
    print("  Open http://127.0.0.1:5000\n")
    app.run(debug=True)
