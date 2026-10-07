"""Public PMCDSTI model interface.

This public-preview file intentionally omits the implementation details of the
prior-calibrated denoising network, temporal modeling block, and spatial dynamic
fusion module while the manuscript is under revision.
"""

import torch.nn as nn


class PMCDSTI(nn.Module):
    """Interface placeholder for the PMCDSTI model.

    The complete implementation will be released after publication.
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        raise NotImplementedError(
            "The full PMCDSTI implementation is withheld during revision and will be released after publication."
        )

    def forward(self, *args, **kwargs):
        raise NotImplementedError

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError
