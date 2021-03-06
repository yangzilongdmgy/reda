"""Dummy data containers for testing purposes."""

import pandas as pd
import numpy as np
import reda

# construct a simple container using random numbers
df = pd.DataFrame(columns=list("ABMNR"))
df.A = np.arange(1, 23)
df.B = df.A + 1
df.M = df.A + 2
df.N = df.B + 2
np.random.seed(0)
df.R = np.random.randn(len(df.R))

ERTContainer = reda.ERT(data=df)

# construct an ERT container with normal and reciprocal data
df = pd.DataFrame(
    [
        # normals
        (0, 1, 2, 4, 3, 1.1),
        (0, 1, 2, 5, 4, 1.2),
        (0, 1, 2, 6, 5, 1.3),
        (0, 1, 2, 7, 6, 1.4),
        (0, 2, 3, 5, 4, 1.5),
        (0, 2, 3, 6, 5, 1.6),
        (0, 2, 3, 7, 6, 1.7),
        (0, 3, 4, 6, 5, 1.8),
        (0, 3, 4, 7, 6, 1.9),
        (0, 4, 5, 7, 6, 2.0),
        # reciprocals
        (0, 4, 3, 1, 2, 1.1),
        (0, 5, 4, 1, 2, 1.2),
        (0, 6, 5, 1, 2, 1.3),
        (0, 7, 6, 1, 2, 1.4),
        (0, 5, 4, 2, 3, 1.5),
        (0, 6, 5, 2, 3, 1.6),
        (0, 7, 6, 2, 3, 1.7),
        (0, 6, 5, 3, 4, 1.8),
        (0, 7, 6, 3, 4, 1.9),
        (0, 7, 6, 4, 5, 2.0),

    ],
    columns=[
        'timestep',
        'A',
        'B',
        'M',
        'N',
        'R',
    ]
)
# now add gaussian noise to the reciprocals
df.loc[10:20, 'R'] += np.random.randn(10)

ERTContainer_nr = reda.ERT(data=df)
