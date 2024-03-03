from app.read_fasta import load_sequence_from_fasta


from Bio.SeqRecord import SeqRecord
from Bio.Seq import MutableSeq, translate, reverse_complement, Seq

def apply_hgvs_mutation(ref_seq, mutation):
    # Convert reference sequence to MutableSeq
    mutable_ref_seq = MutableSeq(str(ref_seq))
    
    # Extract mutation information
    if mutation.startswith('p.'):
        # Protein level mutation
        aa_mutation = mutation[2:]
        aa_from, aa_pos, aa_to = aa_mutation[0], int(aa_mutation[1:-1]), aa_mutation[-1]
        
        # Translate position to DNA level
        codon_start = (aa_pos - 1) * 3
        
        # Mutate the DNA sequence
        codon = mutable_ref_seq[codon_start:codon_start + 3]
        mutated_codon = translate(codon).replace(aa_from, aa_to, 1)
        mutable_ref_seq[codon_start:codon_start + 3] = reverse_complement(mutated_codon).transcribe()
        
    elif mutation.startswith('c.'):
        # DNA level mutation
        dna_mutation = mutation[2:]
        pos_delimiter = next(filter(lambda c: not c.isdigit(), dna_mutation))
        dna_pos = int(dna_mutation[:dna_mutation.index(pos_delimiter)])
        mutation_type = dna_mutation[dna_mutation.index(pos_delimiter) + 1:]
        
        if mutation_type.startswith('del'):
            # Deletion
            del_length = int(mutation_type[3:])
            del_start = dna_pos - 1
            del_end = dna_pos + del_length - 1
            del mutable_ref_seq[del_start:del_end]
        elif mutation_type.startswith('ins'):
            # Insertion
            ins_seq = mutation_type[3:]
            mutable_ref_seq.insert(dna_pos - 1, ins_seq)
        elif mutation_type.startswith('dup'):
            # Duplication
            dup_length = int(mutation_type[3:])
            dup_start = dna_pos - 1
            dup_end = dna_pos + dup_length - 1
            dup_seq = mutable_ref_seq[dup_start:dup_end]
            mutable_ref_seq[dup_start:dup_end] = dup_seq + dup_seq
        elif ">" in mutation_type:
            splice_index = mutation_type.find(">")
            first = mutation_type[:splice_index]
            last = mutation_type[splice_index+1:]
            mutable_ref_seq[dna_pos] = last
        elif "+" in mutation_type:
            parts = mutation.split('+')
            if len(parts) != 2:
                raise ValueError("Invalid mutation format")

            position = int(parts[0])  # Nucleotide position
            mutation_details = parts[1]  # Mutation details (e.g., G>A)

            # Extract the original nucleotide at the mutation position
            original_nucleotide = mutable_ref_seq[position - 1]

            # Check if the original nucleotide matches the expected nucleotide for the mutation
            expected_original_nucleotide = mutation_details.split('>')[0]
            if original_nucleotide != expected_original_nucleotide:
                raise ValueError(f"Unexpected nucleotide at position {position}: {original_nucleotide}")

            # Apply the mutation to create the mutated sequence
            mutable_ref_seq = mutable_ref_seq[:position - 1] + mutation_details.split('>')[1] + mutable_ref_seq[position:]

    # Return mutated sequence
    return SeqRecord(Seq(mutable_ref_seq), id="Mutated ID", description="Mutation of "+ mutation)



def get_mutation(mutation_string, base_file):
    orginal_sequence = load_sequence_from_fasta(base_file)
    sequence = load_sequence_from_fasta(base_file)
    for _mutation in mutation_string.split():
        try:
            sequence = apply_hgvs_mutation(sequence.seq, _mutation)
        except:
            continue
    print([i for i in range(len(orginal_sequence.seq)) if sequence.seq[i] != orginal_sequence.seq[i]])
    return sequence

#get_mutation("c.532C>T", "app/sequence.fasta")
