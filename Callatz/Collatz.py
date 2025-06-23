import matplotlib.pyplot as plt

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

plt.figure(figsize=(12, 8))

for start in range(100, 0, -1):
    sequence = collatz_sequence(start)
    x_vals = list(range(len(sequence)))
    plt.plot(x_vals, sequence, alpha=0.5)

plt.title("Collatz Sequences for Starting Values 100 to 1")
plt.xlabel("Step")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()
