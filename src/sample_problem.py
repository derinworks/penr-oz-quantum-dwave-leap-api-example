"""Example usage of the D-Wave Leap API using the Ocean SDK."""

from __future__ import annotations

import argparse

import dimod

from src.solvers import get_sampler


DEFAULT_NUM_READS = 100


def build_bqm() -> dimod.BinaryQuadraticModel:
    """Create a tiny binary quadratic model for demonstration."""
    linear = {"a": -1, "b": -1}
    quadratic = {("a", "b"): 2}
    return dimod.BinaryQuadraticModel(linear, quadratic, 0.0, dimod.BINARY)


def run_example(solver: str | None, num_reads: int) -> dimod.SampleSet:
    """Submit the BQM to a D-Wave solver and return the response."""
    sampler = get_sampler(solver)
    bqm = build_bqm()
    return sampler.sample(bqm, num_reads=num_reads)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a small D-Wave Leap example.")
    parser.add_argument("--solver", help="Optional solver name from your Leap account.")
    parser.add_argument(
        "--num-reads",
        type=int,
        default=DEFAULT_NUM_READS,
        help="Number of reads to request from the solver.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sampleset = run_example(args.solver, args.num_reads)
    print(sampleset)


if __name__ == "__main__":
    main()
