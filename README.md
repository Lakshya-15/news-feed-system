## Feed Ranking System (WIP)

I’m building a simplified version of how apps like Instagram/Twitter decide:

“What should a user see, and in what order?”

This goes beyond a basic backend — the focus is on feed generation and ranking, not just APIs.

---

## Status

Actively under development with regular commits.

This is a work in progress — things may break, change, or get rewritten as I experiment and learn.

---

## Problem I’m Solving

A feed system has 3 core parts:
- Data → users, posts, follows  
- Retrieval → candidate posts  
- Ranking → what shows up first  

Most projects stop at data. I’m building all three.

---

## Current Direction

- Store posts in the database  
- Generate feed (experimenting with push vs pull)  
- Cache results using Redis  
- Rank posts before returning  

---

## Progress

- Basic schema and APIs  
- Initial ranking logic  
- Feed caching (in progress)  
- Push vs pull strategies (in progress)  
- Async processing (in progress)  
- ML-based ranking (planned)  

---

## Ranking (Current)

```python
score = w1 * recency + w2 * engagement + w3 * affinity

Later I plan to update it with a ML model