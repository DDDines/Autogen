# filename: huskies_adoption_chart.py
import matplotlib.pyplot as plt

# Sample data
months = ['January', 'February', 'March', 'April', 'May', 'June']
huskies_adopted = [10, 15, 12, 18, 20, 25]

plt.figure(figsize=(10, 6))
plt.bar(months, huskies_adopted, color='skyblue')
plt.xlabel('Months')
plt.ylabel('Number of Huskies Adopted')
plt.title('Number of Huskies Adopted in London by Month')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()