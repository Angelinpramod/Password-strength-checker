import tkinter as tk
from core import (rule_based_checks, entropy_calc, entropy_rating, common_pass_check)


def check_pass_gui():
    password = entry.get()

    issues = rule_based_checks(password)
    entropy = entropy_calc(password)
    rating = entropy_rating(entropy)
    is_common = common_pass_check(password)


    output = "-- Password Analysis --\n\n"

    if issues:
        output += "Rule-based issues:\n"
        for issue in issues:
            output += f"- {issue}\n"
    else:
        output += "All rule-based checks passed\n"

    output += f"\nEstimated entropy: {entropy} bits\n"
    output += f"Entropy rating: {rating}\n"
    if is_common:
        output += "\n⚠️ Warning: This password is very commonly used.\n"

    output += "\nNote:\nPassing rule-based checks does NOT guarantee a strong password."

    if rating in ["Very Weak", "Weak"]:
        color = "#ff4d4d"
    elif rating == "Reasonable":
        color = "#ffcc00"
    else:
        color = "#00ff99"

    result_label.config(text=output, fg=color)


# GUI Setup
root= tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x500")
root.configure(bg="#0f0f1a")

title_label =tk.Label(
    root,
    text="Password Strength Checker",
    font=("Courier New",16,"bold"),
    fg="#ff4fd8",        
    bg="#0f0f1a"
)

title_label.pack(pady=15)

entry= tk.Entry(root,show="*" , width=30, font=("Courier New",12), fg="#00ffcc",bg="#1a1a2e",insertbackground="#00ffcc"  )
entry.pack(pady=10)


result_label =tk.Label(
root,
text="",
font=("Courier New", 11),
fg="#ffffff",
bg="#0f0f1a",
justify="left",
wraplength=480
)
result_label.pack(pady=15)


check_button = tk.Button(
    root,
    text="Analyze Password",
    font=("Courier New", 12, "bold"),
    fg="#0f0f1a",
    bg="#ff4fd8",
    activebackground="#ff1fbf",
    activeforeground="#ffffff",
    relief="flat",
    command=check_pass_gui
)

check_button.pack(pady=10)

root.mainloop()
