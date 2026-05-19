## News Feed Ranking System

A backend system that replicates how apps like Instagram/Twitter decide: **”Which posts should a user see, and in what order?”**

The focus is on feed generation and ranking strategy — not just CRUD APIs.

---

## Problem Being Solved

A feed system has 3 core layers:

- **Data** — users, posts, follow graph
- **Retrieval** — which posts are candidates for a user’s feed
- **Ranking** — what order they appear in

Most projects only do the first layer. This one does all three.

---

## Architecture

```
User creates post
    ↓
Store in DB (PostgreSQL)
    ↓
Fan-out to followers (Push model) OR fetch on demand (Pull model)
    ↓
Feed cache updated (Redis sorted sets)
    ↓
User opens app → fetch feed → rank posts → return top N
```

**Key design choices:**
- `api/` — thin layer, only request/response
- `services/` — all business logic lives here
- `workers/` — async fan-out processing
- `cache/` — Redis feed cache, isolated from the rest

---

## Feed Strategies

| Strategy | How | Speed | Trade-off |
|----------|-----|-------|-----------|
| Pull model | Compute feed on read | Slow | Always fresh, simple |
| Push model | Pre-build feed on write | Fast | Write amplification |
| Hybrid | Push for normal users, pull for celebrities | Fast | Handles scale correctly |

---

## Ranking Formula

```python
score = 0.5 * recency + 0.3 * engagement + 0.2 * affinity
```

- **Recency** — `exp(-hours_since_post / 24)`
- **Engagement** — likes + clicks on the post
- **Affinity** — how often the viewer has interacted with this author

Planned: replace formula with a trained logistic regression model.

---

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# copy and edit env file
cp .env.example .env

uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`

---

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/users/` | Create a user |
| POST | `/posts/` | Create a post |
| POST | `/follows/` | Follow a user |
| GET | `/feed/` | Get ranked feed for a user *(coming soon)* |

---

## Build Progress

Currently in **Phase 1 of 7** — laying the foundation (config, models, schemas, dependency injection, route cleanup).
Upcoming phases cover the services layer, Redis caching, push/pull strategies, async processing, observability, and ML-based ranking.

---

## Author

**Lakshya Garg**
garglakshya015@gmail.com
[linkedin.com/in/lakshyagarg1515](https://www.linkedin.com/in/lakshyagarg1515/) · [github.com/Lakshya-15](https://github.com/Lakshya-15)