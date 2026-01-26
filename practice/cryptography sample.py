import asyncio
import pickle
import os
import time
from cryptography.fernet import Fernet

class GhostVault:
    def __init__(self, filename="vault.pkl"):
        self.filename = filename
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def lock(self, secret_message):
        """Encrypts and pickles the message."""
        encrypted_data = self.cipher.encrypt(secret_message.encode())
        with open(self.filename, "wb") as f:
            pickle.dump(encrypted_data, f)
        print(f"\n[SYSTEM] Message locked in {self.filename}.")

    async def monitor_lifespan(self, seconds):
        """The Reaper: Background task that deletes the file after X seconds."""
        print(f"[REAPER] Self-destruct sequence initiated: {seconds}s remaining.")
        await asyncio.sleep(seconds)
        
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("\n[REAPER] TIME EXPIRED. Vault has been vaporized.")
        else:
            print("\n[REAPER] Vault was accessed safely. Reaper standing down.")

    def unlock(self):
        """Unpickles and decrypts the message."""
        if not os.path.exists(self.filename):
            print("\n[ERROR] No vault found. It may have been destroyed.")
            return None
        
        with open(self.filename, "rb") as f:
            encrypted_data = pickle.load(f)
            
        os.remove(self.filename) # Delete after one successful read
        return self.cipher.decrypt(encrypted_data).decode()

async def main():
    vault = GhostVault()
    secret = input("Enter a secret message: ")
    lifespan = int(input("Seconds until self-destruct: "))

    # Lock the message
    vault.lock(secret)

    # Start the background reaper task
    reaper_task = asyncio.create_task(vault.monitor_lifespan(lifespan))

    # Simulate user decision
    choice = input("Type 'OPEN' to read before it's gone: ")
    
    if choice.upper() == "OPEN":
        message = vault.unlock()
        if message:
            print(f"\n[DECRYPTED]: {message}")
        # Cancel the reaper since we finished
        reaper_task.cancel()
    else:
        # Wait for the reaper to finish if the user does nothing
        await reaper_task

if __name__ == "__main__":
    asyncio.run(main())