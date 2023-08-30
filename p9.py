import pandas as pd
import plotly.express as px

excel_file = "skills_data_sam.xlsx"
data = pd.read_excel(excel_file)

color_scale = [
    [0.0, 'lightgreen'],
    [0.2, 'palegreen'],
    [0.4, 'mediumseagreen'],
    [0.6, 'seagreen'],
    [0.8, 'darkseagreen'],
    [1.0, 'darkgreen'],
]

fig = px.treemap(data, path=['SKILL'], values='VAL', color='VAL', color_continuous_scale=color_scale)

fig.update_layout(
    title="Variable-Sized Rectangle TreeMap",
    # width=1000,
    # height=600,
    autosize=True,
)

fig.show()
