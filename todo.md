# Decision Companion Development Plan

## 🔹 Week 1: Sentiment Engine + Decision Logic

### Day 1: Project Setup
- [ ] Create Django project & app
- [ ] Initialize Git repo
- [ ] Create README and define MVP

### Day 2: Sentiment Analysis API
- [ ] Accept multiple texts
- [ ] Return individual sentiment + star rating
- [ ] Validate input format

### Day 3: Decision Logic
- [ ] Create analyze_decision(results)
- [ ] Return "Go ahead" / "Hold off" + reason
- [ ] Add summary to API output

### Day 4: Integrate Logic into API
- [ ] Update API view to include decision layer
- [ ] Add tests for edge cases

### Day 5: JSON & Input Variants
- [ ] Handle malformed or mixed inputs
- [ ] Support basic frontend testing via Postman

### Day 6: Basic Frontend (Optional)
- [ ] Create simple HTML/JS or Django template UI
- [ ] Display sentiment results + decision

### Day 7: Code Review / Refactor
- [ ] Clean up logic and organize into `utils.py`
- [ ] Improve comments and function docs

---

## 🔹 Week 2: Intelligence + Advice Layer

### Day 8: Summary Logic
- [ ] Extract keywords / recurring themes
- [ ] Optionally use GPT/OpenAI to summarize

### Day 9: Expert Advice Engine
- [ ] Simulate expert advice based on sentiment
- [ ] Add prompt templates in `prompts/`

### Day 10: Interactive Q&A API
- [ ] Create `/companion/ask` endpoint
- [ ] Accept user follow-up questions
- [ ] Use GPT or rules to answer based on sentiment data

### Day 11: Context Awareness
- [ ] Add "context" field to input (`product`, `team`, `life`, etc.)
- [ ] Vary decision logic accordingly

### Day 12: UI Enhancements (Optional)
- [ ] Add input for context
- [ ] Display expert advice in UI

### Day 13: Testing + Docs
- [ ] Add more unit tests (utils, views)
- [ ] Create simple API doc (Markdown or Swagger)

### Day 14: Final Polish
- [ ] Clean up code
- [ ] Plan Phase 2 features (auth, DB logging, chatbot)
- [ ] Deploy to Heroku/Railway/Render (if needed)

## Folder structure (optional)
decision_companion/
├── companion/                  # Django app
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py               # (Optional for logging/feedback storage)
│   ├── views.py                # Sentiment & decision logic
│   ├── urls.py                 # App-level routing
│   ├── utils.py                # Helper functions (decision logic, summaries)
│   ├── tests.py                # Unit tests
│   └── prompts/                # Templates for expert advice / summaries
│       └── decision_template.txt
│
├── decision_companion/        # Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/                 # If using Django templates for UI
│   └── companion.html
│
├── static/                    # CSS/JS if needed
│
├── manage.py
├── requirements.txt
└── todo.md                    # Development roadmap
