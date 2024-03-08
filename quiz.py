def ask_question(question, choices, correct_answer):
  """
  Asks a question and returns True if the user answered correctly.

  Args:
    question: The question to ask.
    choices: A list of answer choices.
    correct_answer: The index of the correct answer in the choices list.

  Returns:
    True if the user answered correctly, False otherwise.
  """
  print(question)
  for i, choice in enumerate(choices):
    print(f"{chr(i + 65)}) {choice}")  # Print options with letters (A, B, C, ...)

  while True:
    user_answer = input("Enter your answer (A-B-C...): ").upper()
    if user_answer not in [chr(i+65) for i in range(len(choices))]:
      print("Invalid choice. Please enter an option from A to", chr(len(choices)+64))
    else:
      break

  if user_answer == chr(correct_answer + 65):
    print("Correct!")
    return True
  else:
    print(f"Incorrect. The correct answer is: {choices[correct_answer]}")
    return False

def main():
  """
  Runs the quiz.
  """
  print("Welcome to the quiz!")

  # Define your questions and answers here
  questions = [
    ("Linux is ______", ["Propertiary", "Source-available", "Closed-source", "Free and open-source"], 3),
    ("Which of the following is a Linux distribution?", ["Windows", "macOS", "Fedora", "iOS"], 2),
    ("What is the default package manager for Ubuntu?", ["yum", "apt", "dnf", "pacman"], 1),
    ("What is the default shell for the Linux operating system?", ["Bash", "cmd", "Fish", "PowerShell"], 0),
    ("Which of the following is a programming language?", ["Python", "Java", "C++", "All of the above"], 3),
    ("Which of the following is a web browser?", ["Firefox", "Scribus", "LibreOffice", "All of the above"], 0),
    ("Which of the following is not a desktop environment?", ["GNOME", "KDE", "Tera"], 2),
    ("Ubuntu is a derivative of which Linux distribution?", ["Fedora", "Debian", "openSUSE", "Arch Linux"], 1),
    ("Which of the following is not a virtualization software?", ["VirtualBox", "VMware", "Vintage", "GNOME Boxes"], 2),
    ("Which of the following is not a relational database?", ["MySQL", "PostgreSQL", "SQL Server", "MongoDB"], 3),
    ("Which of the following is not a containerization software?", ["VMWare", "Docker", "Podman"], 0),
    ("Which of the following is not a GUI framework?", ["MAN", "GTK", "Qt"], 0),
    ("Which of the following is not a large language model?", ["Phind", "ChatGPT", "Stable Diffusion", "Google Gemini"], 2),
    ("Which of the following is not an AI image generator?", ["Google Gemini", "Stable Diffusion", "Kramp", "Bing"], 2),
    ("Linux is available in multiple distributions with different features and focuses.", ["True", "False"], 0),
    ("Which of the following statements accurately describes Git?", ["Git is a version control system.", "Git is a programming language."], 0),
    ("Which Linux command is used to change permissions of a file?", ["chown", "chmod", "chgrp", "All of the above"], 1),
    ("What does the acronym 'GUI' stand for in computing?", ["Gaming User Interface", "General User Interface", "Graphical User Interface"], 2),
    ("What does the sudo command do?", ["It allows a user to run commands as another user.", "It allows a user to run commands as the root user.", "It allows a user to run commands as a guest user."], 1),
    ("Which of the following command is used to copy a file securely?", ["ls", "scp", "mv", "rsync"], 1),
    ("What is the purpose of Docker or Podman?", ["To create and manage containers.", "To create and manage virtual machines.", "To create and manage networks."], 0),
    ("What file type should the operating system be in if you plan to run it within VirtualBox?", [".exe", ".iso", ".sh", ".ai"], 1),
    ("Which entity is responsible for the development of Fedora?", ["Red Hat", "Canonical", "SUSE", "Debian"], 0),
    ("Is Windows an open-source operating system?", ["Yes", "No"], 1),
    ("What is the default package manager for Fedora?", ["yum", "apt", "dnf", "pacman"], 2),
    ("What is the command to list files in a directory in Linux?", ["show", "dir", "list", "ls"], 3),
    ("How do you comment out a line of code in Python?", ["//", "..", "#", "$"], 2),
    ("How can you execute a Python script?", ["python script.py", "execute script.py", "run script.py", "open script.py"], 0),
    ("Which of the following is a Python library?", ["Kate", "Pandas", "GNOME Boxes", "Lubuntu"], 1),
    ("What is the command to install a package in Python?", ["pip install", "apt install", "yum install", "dnf install"], 0),
    ("Which of the following is rootless by default?", ["Docker", "Podman"], 1),
    ("Which of the following is true regarding Free and Open-Source Software (FOSS)?", ["FOSS is free to use.", "FOSS is open-source.", "FOSS is free to modify and distribute.", "All of the above"], 3),
    ("How can users contribute to an open-source project?", ["Report bugs.", "Write documentation.", "Submit code.", "All of the above"], 3),
  ]

  score = 0
  for question in questions:
    if ask_question(*question):
      score += 1

  # Calculate and display percentage score
  percentage_score = (score / len(questions)) * 100
  print(f"You answered {score} out of {len(questions)} questions correctly ({percentage_score:.2f}%)")

if __name__ == "__main__":
  main()
