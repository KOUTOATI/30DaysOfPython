import statistics
from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    def sum(self):
        return sum(self.data)
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        n = len(self.data)
        if n == 0:
            return 0
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]
    def mode(self):
        freqs = Counter(self.data)
        max_freq = max(freqs.values())
        return [k for k, v in freqs.items() if v == max_freq]

    def range(self):
        if not self.data:
            return 0
        return max(self.data) - min(self.data)
    def variance(self):
        if len(self.data) < 2:
            return 0
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)
    def standard(self):
        return math.sqrt(self.variance())
    def deviation(self):
        return self.standard()
    def min(self):
        return min(self.data) if self.data else None
    def max(self):
        return max(self.data) if self.data else None
    def count(self):
        return len(self.data)
    def frequency(self):
        return Counter(self.data)

data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(data)

print("Count:", stats.count())
print("Sum:", stats.sum())
print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Range:", stats.range())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.standard())
print("Min:", stats.min())
print("Max:", stats.max())
print("Frequency Distribution:", stats.frequency())


class PersonAccount:
    def _init_(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def add_income(self, description, amount):
        self.incomes.append((description, amount))

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def total_income(self):
        return sum(amount for _, amount in self.incomes)

    def total_expense(self):
        return sum(amount for _, amount in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"{self.firstname} {self.lastname} - Solde: {self.account_balance()} €"
