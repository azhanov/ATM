# ATM

## Boilerplate implementation of an ATM machine basic functionality in code.

Given 4 essential functional requirements:
- A customer can login to the ATM account by providing a 4 digit pin number
- A customer can view their current balance
- A customer can deposit money 
- A customer can withdraw money

Let's add one more practical one:
- Daily withdrawl limit

## Non functional requirements
- Any changes must be persisted to a permanent storage
- Distributed lock, to make things easier let's quote https://redis.io/topics/distlock:
>1. Safety property: Mutual exclusion. At any given moment, only one client can hold a lock.
>2. Liveness property A: Deadlock free. Eventually it is always possible to acquire a lock, even if the client that locked a resource crashes or gets partitioned.
>3. Liveness property B: Fault tolerance. As long as the majority of Redis nodes are up, clients are able to acquire and release locks.

Thus, when a user logs into an ATM, other users with the same PIN can not login/perform any activities until currently logged in user either logs out or connection times out.

## Implementation

# Naive
Due to it's simplicity, naive implementtion is written in Python as a straight forward script that only implements functional requirements, while omitting all the non-functional ones. 

# Better
Better implementation is proposed to be written in Java. GlobalLock provides simple interface, and GlobalLockFile provides a simple NIO based locking implementation. This is to address the "Safety property" from the Distributed lock requirements. However, it obviously only works in the context of a single machine.

# Best
Future implementation - use a trully distributed lock (a DB "select for update..." exclusive lock or Redis distlock mentioned above) to achieve trully distributed lock requirements.

Makes sense? Throw me a question otherwise.
Thanks and happy coding!
