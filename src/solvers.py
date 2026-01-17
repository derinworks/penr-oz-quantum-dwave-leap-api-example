"""Helpers for configuring D-Wave Leap solvers."""

from __future__ import annotations

from typing import Optional

from dwave.system import DWaveSampler, EmbeddingComposite


def get_sampler(solver: Optional[str] = None) -> EmbeddingComposite:
    """Return an embedding composite sampler using the Leap credentials."""
    if solver:
        base_sampler = DWaveSampler(solver=solver)
    else:
        base_sampler = DWaveSampler()

    return EmbeddingComposite(base_sampler)
