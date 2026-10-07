"""Dataset interface placeholder for dataset_pemsbay.

The full preprocessing and masking implementation is withheld during the manuscript revision stage.
This file documents the expected public interface only.
"""


def get_dataloader(*args, **kwargs):
    """Return train/validation/test dataloaders.

    Full data preprocessing code will be released after publication.
    """
    raise NotImplementedError(
        "The full dataset loader is withheld during revision and will be released after publication."
    )
