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

    def load_sample(self):
        self.students.clear()
        sample = [("Alice", 92), ("Bob", 76), ("Carol", 58), ("David", 84),
                  ("Emma", 45), ("Frank", 67), ("Grace", 99), ("Henry", 31)]
        for name, marks in sample:
            self.students.append((name, marks))

    def get_marks_array(self):
        return np.array([marks for _, marks in self.students])

    def get_names(self):
        return [name for name, _ in self.students]

    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A+"
        if marks >= 80:
            return "A"
        if marks >= 70:
            return "B"
        if marks >= 60:
            return "C"
        if marks >= 50:
            return "D"
        if marks >= 40:
            return "E"
        return "F"

    def grade_distribution(self):
        order = ["A+", "A", "B", "C", "D", "E", "F"]
        counts = {g: 0 for g in order}
        for _, marks in self.students:
            counts[self.grade(marks)] += 1
        return {g: counts[g] for g in order if counts[g] > 0}

    def pass_rate(self):
        if not self.students:
            return 0.0
        passed = sum(1 for _, m in self.students if m >= 40)
        return 100.0 * passed / len(self.students)

    def analyze(self):
        marks = self.get_marks_array()
        if marks.size == 0:
            return None
        
        return {
            "max": np.max(marks),
            "min": np.min(marks),
            "mean": np.mean(marks),
            "sum": np.sum(marks),
            "std": np.std(marks),
            "median": np.median(marks),
            "pass": self.pass_rate()
        }
