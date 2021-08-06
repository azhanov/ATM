package com.alexz.atm;

import java.nio.channels.FileLock;

public interface GlobalLock {
    FileLock acquireLock(int pin);
    boolean releaseLock(int pin);
}
