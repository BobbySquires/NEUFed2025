"""
Standalone utility functions, some for Plotly, some for other stuff
"""

import plotly.graph_objects as go 
import plotly.io as pio

def add_end_labels(fig:go.Figure, offset:float =0.0, **text_kwargs) -> None:
    """
    Adds end labels and markers to scatter line traces in a Plotly figure.
    Label and marker colors match the line color, including those set by templates.
    
    Parameters:
        fig: plotly.graph_objects.Figure
        offset: float vertical offset for labels (fraction of y-range)
        **text_kwargs: passed to go.layout.Annotation
    """
    # Use template from the figure layout or default
    if fig.layout.template: # type: ignore
        template = fig.layout.template # type: ignore
    else:
        template = pio.templates[pio.templates.default]
        
    colorway = template.layout.colorway or pio.templates["plotly"].layout.colorway # type: ignore

    color_idx = 0  # To track which color from the colorway to use

    for trace in fig.data:
        if not (hasattr(trace, 'x') and hasattr(trace, 'y')):
            continue
        if len(trace.x) == 0 or len(trace.y) == 0:
            continue
        if not (hasattr(trace, 'mode') and 'lines' in trace.mode):
            continue

        x_end = trace.x[-1]
        y_end = trace.y[-1]
        y_range = max(trace.y) - min(trace.y) if len(trace.y) > 1 else 1

        # Get color: use explicitly set color, or infer from template colorway
        if trace.line.color:
            color = trace.line.color
        else:
            color = colorway[color_idx % len(colorway)]
            color_idx += 1

        # Add text label
        label = f"{y_end:.2f}"
        fig.add_annotation(
            x=x_end,
            y=y_end + offset * y_range,
            text=label,
            showarrow=False,
            font=dict(color=color),
            xanchor='left',
            yanchor='middle',
            xshift=6,
            **text_kwargs
        )

        # Add marker at end TODO this isn't working right now, fix later
        fig.add_trace(go.Scatter(
            x=[x_end],
            y=[y_end],
            mode='markers',
            marker=dict(
                symbol='circle',
                size=8,
                color=color
                ),
            showlegend=False,
            zorder=3, # Not sure whats wrong here??
            hoverinfo='skip'
        ))

# path_utils.py
from pathlib import Path

def get_repo_root() -> Path:
    """
    Moves up the repo to get the git root path and returns it

    Returns:
        Path: Absolute path to the root of the Git repo.

    Raises:
        FileNotFoundError: If the .git directory doesnt exist
    """
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists():
            return parent
    raise FileNotFoundError("Could not find .git directory")