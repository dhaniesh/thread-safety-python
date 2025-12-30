# thread-safety-python

This project demonstrates thread safety by modifying a shared mutable resource accessed concurrently by multiple threads.
The unsafe version shows a race condition caused by non-atomic read–modify–write operations.
The safe version uses a lock to enforce mutual exclusion