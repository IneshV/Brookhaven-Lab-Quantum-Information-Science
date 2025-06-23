import numpy as np
import plotly.graph_objects as go

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def find_local_extrema(seq):
    maxima = []
    minima = []
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            maxima.append((i, seq[i]))
        elif seq[i] < seq[i-1] and seq[i] < seq[i+1]:
            minima.append((i, seq[i]))
    return maxima, minima

# Generate and pad sequences
sequences = [collatz_sequence(n) for n in range(100, 0, -1)]
max_len = max(len(seq) for seq in sequences)
padded_sequences = [
    [None] * (max_len - len(seq)) + seq for seq in sequences
]

fig = go.Figure()

# Plot all sequences
for start, seq in zip(range(100, 0, -1), padded_sequences):
    x = list(range(max_len))
    fig.add_trace(go.Scatter(x=x, y=seq, mode='lines', name=f'{start}', opacity=0.5, line=dict(width=1)))

    # Highlight extrema
    maxima, minima = find_local_extrema([v for v in seq if v is not None])
    shift = max_len - len(seq)
    for x_val, y_val in maxima:
        fig.add_trace(go.Scatter(
            x=[x_val + shift], y=[y_val],
            mode='markers',
            marker=dict(color='red', size=6),
            name=f'Max at {start}',
            hovertemplate=f"Max<br>Step: {x_val + shift}<br>Value: {y_val}<extra></extra>"
        ))
    for x_val, y_val in minima:
        fig.add_trace(go.Scatter(
            x=[x_val + shift], y=[y_val],
            mode='markers',
            marker=dict(color='blue', size=6),
            name=f'Min at {start}',
            hovertemplate=f"Min<br>Step: {x_val + shift}<br>Value: {y_val}<extra></extra>"
        ))

fig.update_layout(
    title="Collatz Sequences (100 to 1) — Aligned by Endpoint with Extrema",
    xaxis_title="Step (ending at 1)",
    yaxis_title="Value",
    hovermode="closest",
    showlegend=False,
    height=700
)

fig.show()
