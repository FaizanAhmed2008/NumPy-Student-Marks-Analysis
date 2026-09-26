import numpy as np

class MarksAnalysis:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        self.students.append((name, marks))

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            del self.students[index]

    def clear_all(self):
        self.students.clear()

    def get_marks_array(self):
        return np.array([marks for _, marks in self.students])

    def get_names(self):
        return [name for name, _ in self.students]

    def analyze(self):
        marks = self.get_marks_array()
        if marks.size == 0:
            return None
        
        return {
            "max": np.max(marks),
            "min": np.min(marks),
            "mean": np.mean(marks),
            "sum": np.sum(marks),
            "std": np.std(marks)
        }
