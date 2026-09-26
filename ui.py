import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from analysis import MarksAnalysis

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NumPy Student Marks Analysis")
        self.geometry("950x750")
        self.configure(bg="#1e1e1e")
        
        self.analysis = MarksAnalysis()
        
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        
        # Professional Dark Theme Colors (VS Code inspired)
        self.bg_color = "#1e1e1e"
        self.frame_bg = "#252526"
        self.text_color = "#cccccc"
        self.heading_color = "#ffffff"
        self.accent_color = "#007acc"
        self.accent_hover = "#005f9e"
        self.danger_color = "#f44336"
        self.danger_hover = "#d32f2f"
        self.success_color = "#4caf50"
        self.warning_color = "#ff9800"
        
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color, font=("Segoe UI", 11))
        self.style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"), foreground=self.heading_color)
        self.style.configure("Treeview", background=self.frame_bg, foreground=self.text_color, fieldbackground=self.frame_bg, rowheight=28, borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#04395e')], foreground=[('selected', self.heading_color)])
        self.style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#333333", foreground=self.heading_color, borderwidth=0)
        
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="25")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Label(main_frame, text="NumPy Student Marks Analysis", style="Header.TLabel")
        header.pack(pady=(0, 25), anchor="w")
        
        # Top section: Input and Dashboard
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 25))
        
        # Input Section
        input_frame = tk.LabelFrame(top_frame, text=" Add Student Record ", bg=self.bg_color, fg=self.accent_color, font=("Segoe UI", 12, "bold"), bd=1, relief="solid")
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        ttk.Label(input_frame, text="Student Name:").grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(input_frame, textvariable=self.name_var, bg=self.frame_bg, fg=self.heading_color, font=("Segoe UI", 11), insertbackground=self.heading_color, relief="flat", highlightthickness=1, highlightbackground="#3c3c3c", highlightcolor=self.accent_color)
        self.name_entry.grid(row=0, column=1, padx=15, pady=15, sticky="ew", ipady=4)
        
        ttk.Label(input_frame, text="Marks (0-100):").grid(row=1, column=0, padx=15, pady=10, sticky="w")
        self.marks_var = tk.StringVar()
        self.marks_entry = tk.Entry(input_frame, textvariable=self.marks_var, bg=self.frame_bg, fg=self.heading_color, font=("Segoe UI", 11), insertbackground=self.heading_color, relief="flat", highlightthickness=1, highlightbackground="#3c3c3c", highlightcolor=self.accent_color)
        self.marks_entry.grid(row=1, column=1, padx=15, pady=10, sticky="ew", ipady=4)
        
        add_btn = tk.Button(input_frame, text="Add Student", command=self.add_student, bg=self.accent_color, fg="white", font=("Segoe UI", 11, "bold"), borderwidth=0, padx=15, pady=8, cursor="hand2", activebackground=self.accent_hover, activeforeground="white")
        add_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        input_frame.columnconfigure(1, weight=1)
        
        # Dashboard Section
        dash_frame = tk.LabelFrame(top_frame, text=" Analysis Dashboard ", bg=self.bg_color, fg=self.accent_color, font=("Segoe UI", 12, "bold"), bd=1, relief="solid")
        dash_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))
        
        self.dash_labels = {}
        stats = ["Maximum", "Minimum", "Average", "Total", "Std Dev"]
        for i, stat in enumerate(stats):
            ttk.Label(dash_frame, text=f"{stat}:", font=("Segoe UI", 11, "bold")).grid(row=i//2, column=(i%2)*2, padx=15, pady=12, sticky="e")
            val_lbl = ttk.Label(dash_frame, text="-", font=("Segoe UI", 12, "bold"), foreground=self.accent_color)
            val_lbl.grid(row=i//2, column=(i%2)*2+1, padx=15, pady=12, sticky="w")
            self.dash_labels[stat] = val_lbl
            
        btn_frame = ttk.Frame(dash_frame)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=15)
        
        analyze_btn = tk.Button(btn_frame, text="Analyze Marks", command=self.update_analysis, bg=self.success_color, fg="white", font=("Segoe UI", 11, "bold"), borderwidth=0, padx=15, pady=8, cursor="hand2", activebackground="#388e3c", activeforeground="white")
        analyze_btn.pack(side=tk.LEFT, padx=10)
        
        graph_btn = tk.Button(btn_frame, text="View Graph", command=self.show_graph, bg=self.warning_color, fg="white", font=("Segoe UI", 11, "bold"), borderwidth=0, padx=15, pady=8, cursor="hand2", activebackground="#f57c00", activeforeground="white")
        graph_btn.pack(side=tk.LEFT, padx=10)
        
        # Table Section
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("#", "Name", "Marks")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("#", text="Student No.")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Marks", text="Marks")
        
        self.tree.column("#", width=100, anchor="center")
        self.tree.column("Name", width=500, anchor="w")
        self.tree.column("Marks", width=150, anchor="center")
        
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bottom Buttons
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=(20, 0))
        
        remove_btn = tk.Button(bottom_frame, text="Remove Selected", command=self.remove_student, bg=self.frame_bg, fg=self.text_color, font=("Segoe UI", 10), borderwidth=1, padx=15, pady=6, cursor="hand2", activebackground="#333333", activeforeground="white", highlightbackground="#3c3c3c")
        remove_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = tk.Button(bottom_frame, text="Clear All", command=self.clear_all, bg=self.danger_color, fg="white", font=("Segoe UI", 10, "bold"), borderwidth=0, padx=15, pady=6, cursor="hand2", activebackground=self.danger_hover, activeforeground="white")
        clear_btn.pack(side=tk.RIGHT)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, (name, marks) in enumerate(self.analysis.students, start=1):
            self.tree.insert("", tk.END, values=(i, name, marks))

    def add_student(self):
        name = self.name_var.get().strip()
        marks_str = self.marks_var.get().strip()
        
        if not name:
            messagebox.showerror("Validation Error", "Student name cannot be empty.")
            return
            
        try:
            marks = float(marks_str)
        except ValueError:
            messagebox.showerror("Validation Error", "Marks must be a numeric value.")
            return
            
        if not (0 <= marks <= 100):
            messagebox.showerror("Validation Error", "Marks must be between 0 and 100.")
            return
            
        self.analysis.add_student(name, marks)
        self.refresh_table()
        self.name_var.set("")
        self.marks_var.set("")
        self.name_entry.focus()
        
    def remove_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to remove.")
            return
            
        item = selected[0]
        values = self.tree.item(item, 'values')
        index = int(values[0]) - 1
        self.analysis.remove_student(index)
        self.refresh_table()
        self.reset_dashboard()
        
    def clear_all(self):
        if not self.analysis.students:
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all student records?"):
            self.analysis.clear_all()
            self.refresh_table()
            self.reset_dashboard()
            
    def update_analysis(self):
        res = self.analysis.analyze()
        if not res:
            messagebox.showinfo("Info", "No data to analyze. Please add students first.")
            self.reset_dashboard()
            return
            
        self.dash_labels["Maximum"].config(text=f"{res['max']:.2f}")
        self.dash_labels["Minimum"].config(text=f"{res['min']:.2f}")
        self.dash_labels["Average"].config(text=f"{res['mean']:.2f}")
        self.dash_labels["Total"].config(text=f"{res['sum']:.2f}")
        self.dash_labels["Std Dev"].config(text=f"{res['std']:.2f}")
        
    def reset_dashboard(self):
        for lbl in self.dash_labels.values():
            lbl.config(text="-")
            
    def show_graph(self):
        names = self.analysis.get_names()
        marks = self.analysis.get_marks_array()
        
        if len(names) == 0:
            messagebox.showinfo("Info", "No data to graph. Please add students first.")
            return
            
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Professional graph styling
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        
        bars = ax.bar(names, marks, color='#007acc', width=0.6)
        
        ax.set_title('Student Marks Distribution', fontsize=14, pad=20, color='white', fontweight='bold')
        ax.set_xlabel('Students', fontsize=12, labelpad=10)
        ax.set_ylabel('Marks', fontsize=12, labelpad=10)
        ax.set_ylim(0, 105)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#555555')
        ax.spines['bottom'].set_color('#555555')
        
        ax.grid(axis='y', color='#333333', linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', va='bottom', fontsize=10, color='white')
            
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
