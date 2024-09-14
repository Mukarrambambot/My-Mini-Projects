import pyautogui
import time
import tkinter as tk
from tkinter import scrolledtext
import threading
import sys
from M_BotAI import Assistant  # Import your assistant class from M_Bot_AI.py
sys.path.append("..")  # To access the parent directory


class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("M_BotAI")
        
        self.chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.user_input = tk.Entry(root, width=40)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.assistant = Assistant()  # Instantiate your assistant class

def send_message(self):
    user_query = self.user_input.get()
    self.user_input.delete(0, tk.END)
    self.update_chat_history(f"You: {user_query}")

    if user_query.lower() == "exit":
        self.assistant.exit()  # Call the exit method
        self.root.destroy()  # Close the GUI window
        return

    assistant_response = self.assistant.process_query(user_query)
    self.update_chat_history(f"M_Bot AI: {assistant_response}")

    def update_chat_history(self, message):
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.see(tk.END)

    def type_in_whatsapp(self, contact_name, message):
        # Activate WhatsApp window (assuming it's already open)
        # You might need to adjust the coordinates based on your screen resolution and WhatsApp window size
        pyautogui.click(x=100, y=100)  # Click on a corner of the screen to activate WhatsApp window
        time.sleep(1)  # Add a small delay to ensure WhatsApp is active

        # Type the contact name
        pyautogui.write(contact_name)
        pyautogui.press('enter')
        time.sleep(1)  # Add a small delay to ensure the chat is opened

        # Type the message
        pyautogui.write(message)
        pyautogui.press('enter')

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()
