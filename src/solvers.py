"""Helpers for configuring D-Wave Leap solvers."""

from __future__ import annotations

import os
from typing import Optional

from dwave.system import DWaveSampler, EmbeddingComposite


class MissingLeapTokenError(RuntimeError):
    """Raised when the DWAVE_API_TOKEN environment variable is missing."""


def get_sampler(solver: Optional[str] = None) -> EmbeddingComposite:
    """Return an embedding composite sampler using the Leap credentials."""
    token = os.environ.get("DWAVE_API_TOKEN")
    if not token:
        raise MissingLeapTokenError(
            "DWAVE_API_TOKEN is not set. Set it to your Leap API token before running."
        )

    if solver:
        base_sampler = DWaveSampler(solver=solver)
    else:
        base_sampler = DWaveSampler()

    return EmbeddingComposite(base_sampler)
