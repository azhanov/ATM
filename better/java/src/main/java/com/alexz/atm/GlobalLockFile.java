package com.alexz.atm;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.logging.Level;
import java.util.logging.Logger;

public class GlobalLockFile implements GlobalLock {

    FileLock fileLock;
    FileChannel fileChannel;
    private static final Logger LOGGER = Logger.getLogger(GlobalLockFile.class.getName());

    GlobalLockFile() {
        LOGGER.setLevel(Level.FINE);
        fileLock = null;
        fileChannel = null;
    }

    @Override
    public FileLock acquireLock(int pin) {
        Path path = this.getLockFile(pin);

        try {
            RandomAccessFile randomAccessFile = new RandomAccessFile(path.toString(), "rw");
            fileChannel = randomAccessFile.getChannel();
            fileLock = fileChannel.tryLock();

            if (fileLock != null) {
                LOGGER.info("Acquired lock: " + fileLock);
            } else {
                LOGGER.warning("Couldn't acquired lock, currently lock=null");
            }
        }
        catch (Exception ex) {
            LOGGER.log(Level.SEVERE,"Error occurred when acquiring file lock and closing file.", ex);
        }
        LOGGER.info("Acquired lock: " + fileLock);
        return fileLock;
    }

    @Override
    public boolean releaseLock(int pin) {
        boolean result;
        if (fileChannel != null && fileLock != null) {
            try {
                fileLock.release();
                fileChannel.close();
                result = true;
                //IOUtils.closeQuietly(outputStream);
            } catch (IOException e) {
                LOGGER.log(Level.SEVERE,"Error occurred when releasing file lock and closing file.", e);
                result = false;
            }
        } else {
            LOGGER.info("Can not release a lock, channel = " + fileChannel + " and lock = " + fileLock);
            result = false;
        }
        return result;
    }

    private Path getLockFile(int pin) {
        String strTmp = System.getProperty("java.io.tmpdir");
        Path lockFilePath = Paths.get(strTmp, pin + ".lock");
        try {
            Files.createFile(lockFilePath);
            return lockFilePath;
        } catch (FileAlreadyExistsException fae) {
            LOGGER.info("File already exists");
            return lockFilePath;
        } catch (IOException ioe) {
            LOGGER.log(Level.SEVERE, "Exception occurred", ioe);
            return null;
        }
    }

    public static void main(String[] args) {
        GlobalLockFile glf = new GlobalLockFile();
        FileLock fileLock = glf.acquireLock(1234);
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("After sleep Acquired lock: " + fileLock);
    }
}
