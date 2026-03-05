# import time

# text = "Python is powerful and easy to learn"

# print("Type the following text:")
# print(text)


# input("Press Enter when you are ready...")

# start_time = time.time()
# user_input = input("Start typing: ")

# end_time = time.time()

# time_taken =  end_time - start_time

# print("Time taken:", time_taken, "seconds")

# word_count = len(user_input.split())

# print("Word count:", word_count)

# wpm = (word_count / time_taken) * 60

# print("WPM",wpm)

# if user_input == text:
#     print("Accuracy: 100%")
# else:
#     print("There were mistakes.")
import tkinter as tk
import time

root = tk.Tk()
root.title("Wpm Typing test")
root.geometry("500x350")

text_to_type = "Python is powerful and easy to learn"

label = tk.Label(root, text=text_to_type, wraplength=400, font=("Arial", 14))
label.pack(pady=20)

text_box = tk.Text(root, height=5, width=50, font=("Arial", 12))
text_box.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

def start_test():
    global start_time
    start_time = time.time()
    result_label.config(text="Test Started!")

start_button = tk.Button(root, text="Start Test", command=start_test)
start_button.pack()

def submit_test():
    if 'start_time' not in globals():
        result_label.config(text="Press Start first!")
        return

    end_time = time.time()
    time_taken = end_time - start_time

    user_input = text_box.get("1.0", tk.END).strip()

    word_count = len(user_input.split())
    wpm = (word_count / time_taken) * 60

    if user_input == text_to_type:
        accuracy = 100
    else:
        accuracy = 0

    result_label.config(
        text=f"Time: {time_taken:.2f} sec\nWPM: {wpm:.2f}\nAccuracy: {accuracy}%"
    )

submit_button = tk.Button(root, text="Submit", command=submit_test)
submit_button.pack(pady=5)

root.mainloop()