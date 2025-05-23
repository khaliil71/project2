# project2
@@ -0,0 +1,81 @@
import tkinter as tk
from tkinter import ttk
from workout_logic import WorkoutLogic


class WorkoutGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Beginner Workout Planner")
        self.root.geometry("500x500")

        self.logic = WorkoutLogic()
        self.create_widgets()

    def create_widgets(self):
       
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

       
        ttk.Label(main_frame,
                  text="3-Day Beginner Workout Plan",
                  font=('Arial', 16, 'bold')).pack(pady=10)

       
        ttk.Label(main_frame,
                  text="This is a simple starter plan for absolute beginners.",
                  wraplength=400).pack(pady=5)

   
        ttk.Button(main_frame,
                   text="Show My Workout Plan",
                   command=self.show_plan).pack(pady=15)

      
        results_frame = ttk.LabelFrame(main_frame,
                                       text="Your 3-Day Plan",
                                       padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)

        self.results = tk.Text(results_frame,
                               height=15,
                               wrap=tk.WORD,
                               padx=5,
                               pady=5,
                               font=('Arial', 10))

        scrollbar = ttk.Scrollbar(results_frame,
                                  command=self.results.yview)
        self.results.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results.pack(fill=tk.BOTH, expand=True)

       
        self.results.tag_config('day', font=('Arial', 12, 'bold'), foreground='blue')
        self.results.tag_config('exercise', font=('Arial', 10))
        self.results.tag_config('cardio', foreground='green')

    def show_plan(self):
        plan = self.logic.get_beginner_plan()

      

        for day in plan:
            self.results.insert(tk.END, f"\n{day['day']}\n", 'day')

            for exercise in day['exercises']:
                if 'duration' in exercise:
                    self.results.insert(tk.END,
                                        f"  • {exercise['name']}: {exercise['duration']}\n",
                                        'cardio')
                elif 'sets' in exercise:
                    self.results.insert(tk.END,
                                        f"  • {exercise['name']}: {exercise['sets']} x {exercise['reps']}\n",
                                        'exercise')
                else:
                    self.results.insert(tk.END,
                                        f"  • {exercise['name']}\n",
                                       
