import tkinter as tk
import openai
import threading

def send_message(event=None):
    user_content = user_input.get()
    user_input.delete(0, tk.END)
    messages.append({"role": "user", "content": f"{user_content}"})
    update_chat_log(f"User: {user_content}\n")

    thread = threading.Thread(target=get_chatbot_response, args=(messages,))
    thread.start()

def get_chatbot_response(messages):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    chat_log.after(0, update_chat_log, f"GPT: {assistant_content}\n")

def update_chat_log(text):
    chat_log.configure(state=tk.NORMAL)
    chat_log.insert(tk.END, text)
    chat_log.configure(state=tk.DISABLED)
    chat_log.yview(tk.END)

openai.api_key = "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"

root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("600x350")
root.configure(bg="pink")


# 대화기록 창
chat_frame = tk.Frame(root)
chat_frame.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)

chat_log = tk.Text(chat_frame, width=80, height=20, state=tk.DISABLED)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_log.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_log.yview)

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, fill=tk.X)
input_frame.configure(width=200, height=100, bg="light blue")

user_input = tk.Entry(input_frame, width=55)
user_input.pack(side=tk.LEFT, padx=5, pady=5)
user_input.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

messages = [{"role": "assistant", "content": "안녕하세요! 저는 OpenAI 챗봇입니다. 어떻게 도와드릴까요?"}]
update_chat_log("GPT: 안녕하세요! 저는 OpenAI 챗봇입니다. 어떻게 도와드릴까요?\n")

root.mainloop()