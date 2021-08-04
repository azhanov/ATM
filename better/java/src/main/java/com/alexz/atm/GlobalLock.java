package com.alexz.atm;

import java.nio.channels.FileLock;

public interface GlobalLock {
    public FileLock acquireLock(int pin);
    public boolean releaseLock(int pin);
}
