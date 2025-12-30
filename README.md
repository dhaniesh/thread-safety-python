# thread-safety-python

- This project demonstrates thread safety by modifying a shared mutable resource accessed concurrently by multiple threads.

- The unsafe version shows a race condition caused by non-atomic read–modify–write operations. The safe version uses a lock to enforce mutual exclusion

- Integer addition operations in Python are executed as a sequence of bytecode instructions. GIL ensures only one thread is allowed to access Python bytecode at a time, so simple integer addition operation is atomic. To allow other threads to run, time.sleep(0) is added, which yields control to other threads to run.