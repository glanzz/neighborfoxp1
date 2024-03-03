from Bio import SeqIO

def load_sequence_from_fasta(fasta_file):
    """
    Load sequence from a FASTA file using Biopython.

    Args:
    - fasta_file (str): The path to the FASTA file.

    Returns:
    - Bio.SeqRecord.SeqRecord: A SeqRecord object representing the sequence.
    """
    try:
        record = SeqIO.read(fasta_file, "fasta")
        return record
    except Exception as e:
        print("Error occurred while loading sequence from FASTA file:", str(e))



'''
sequence_record = load_sequence_from_fasta(path)
if sequence_record:
    print("Sequence ID:", sequence_record.id)
    print("Sequence description:", sequence_record.description)
    print("Sequence length:", len(sequence_record))
    print("Sequence:")
    #print(sequence_record.seq)
'''