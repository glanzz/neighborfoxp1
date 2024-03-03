from Bio import pairwise2
import numpy as np
from Bio.Align import PairwiseAligner
from Bio.SeqUtils import gc_fraction

def GC(sequence):
    return 100 * gc_fraction(sequence, ambiguous="ignore")

def get_sequence_aligment_identity(sequence1, sequence2):

  # Perform pairwise sequence alignment
  alignments = pairwise2.align.globalxx(sequence1, sequence2)

  # Assuming only one alignment for simplicity
  alignment = alignments[0]

  # Calculate alignment score (number of matches)
  alignment_score = alignment[2]

  # Calculate percent identity
  percent_identity = (alignment_score / len(sequence1)) * 100

  return alignment_score, percent_identity


def sequence_similarity(seq1, seq2):
    aligner = PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    best_alignment = max(alignments, key=lambda x: x.score)
    similarity = best_alignment.score / len(seq1) * 100
    return similarity

def mutation_type(seq1, seq2):
    if seq1 == seq2:
        return "No Mutation"
    elif len(seq1) == len(seq2):
        return "Substitution"
    elif len(seq1) > len(seq2):
        return "Deletion"
    else:
        return "Insertion"

def nucleotide_diversity(seq1, seq2):
    diffs = sum(1 for a, b in zip(seq1, seq2) if a != b)
    return diffs / len(seq1)

def genetic_distance(seq1, seq2):
    diffs = sum(1 for a, b in zip(seq1, seq2) if a != b)
    return -np.log(1 - (2 * (diffs / len(seq1))))


def indel_length_frequency(seq1, seq2):
    indels = []
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a != b:
            start = i
            while i < len(seq1) and seq1[i] != seq2[i]:
                i += 1
            end = i
            indels.append(end - start)
    indel_lengths = np.array(indels)
    avg_length = np.mean(indel_lengths)
    frequency = len(indels) / len(seq1)
    return avg_length, frequency

def transition_transversion_ratio(seq1, seq2):
    transitions = transversions = 0
    for a, b in zip(seq1, seq2):
        if (a, b) in [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]:
            transitions += 1
        elif a != b:
            transversions += 1
    return transitions / transversions

def heterozygosity(seq):
    total_sites = len(seq)
    heterozygous_sites = sum(1 for base in seq if base in ("R", "Y", "S", "W", "K", "M"))
    return heterozygous_sites / total_sites