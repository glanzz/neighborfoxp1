# Import necessary libraries and modules
from app import util, attributing_util
from app.read_fasta import load_sequence_from_fasta
from app.generate_structure import get_mutation

FOXP1_FASTA_FILE = "app/sequence.fasta" 
COMPARISION_ALLOWABLE = ["foxp1", "foxp4"]


def predict_mutation_effect(mutation):
    '''
    Load all wild type sequesnces associated with foxp1 and its neighbours
    Get the correlation metrics for all of by comparing the sequence with the other ones
    compare it with the actual foxp1 standard
    Determine the observability and its changes due to this
    '''
    mutation_bonding_factors = {}
    for allowable_comparator in COMPARISION_ALLOWABLE:
        file_name = f"app/{allowable_comparator}.fasta"

        wild_type_sequence = load_sequence_from_fasta(file_name)
        mutant_sequence = get_mutation(mutation, FOXP1_FASTA_FILE)

        changing_positions = []
        for i in range(len(wild_type_sequence.seq)):
            if i < len(mutant_sequence.seq):
                break
            if wild_type_sequence.seq[i] != mutant_sequence.seq[i]:
                changing_positions.append(i)

        # Predict effect on DNA binding, dimerization, and protein-protein interactions
        dna_binding_effect = 0
        for motif in util.get_motifs():
            dna_binding_effect += util.get_binding_affinity(wild_type_sequence.seq, mutant_sequence=mutant_sequence.seq, binding_motif=motif)
        try:
            alignment_score, percent_identity = attributing_util.get_sequence_aligment_identity(wild_type_sequence.seq, mutant_sequence.seq)
        except:
            alignment_score, percent_identity = 0,0

        original_gc_content = attributing_util.GC(mutant_sequence)
        wild_type_sequence_gc_content = attributing_util.GC(wild_type_sequence)
        

        #dna_binding_effect = seq. (wild_type_residue, mutant_residue)
        #dimerization_effect = ppi.predict_dimerization_effect(wild_type_structure, mutant_structure)
        #interaction_effect = ppi.predict_interaction_effect(wild_type_structure, mutant_structure)
        
        mutation_bonding_factors[allowable_comparator] = {
            "DNA BINDING_EFFECT": dna_binding_effect,
            "CHANGING_POSITIONS": changing_positions,
            "ALIGNMENT_SCORE": alignment_score,
            "PERCENTAGE_IDENTITY": percent_identity,
            "M_GC": original_gc_content,
            "C_GC": wild_type_sequence_gc_content,
            "M_HETEROZYGOSITY": attributing_util.heterozygosity(mutant_sequence.seq),
            "C_HETEROZYGOSITY": attributing_util.heterozygosity(wild_type_sequence.seq),
            "TRANSITION_TRAVERSION_RATIO": attributing_util.transition_transversion_ratio(wild_type_sequence.seq, mutant_sequence.seq),
            #"INDEL_LENGTH_FREQUENCY": attributing_util.indel_length_frequency(wild_type_sequence.seq, mutant_sequence.seq),
            "GENETIC_DISTANCE": attributing_util.genetic_distance(wild_type_sequence.seq, mutant_sequence.seq),
            "NUCLEOTIDE_DIVERSITY": attributing_util.nucleotide_diversity(wild_type_sequence.seq, mutant_sequence.seq),
            "MUTATION_TYPE": attributing_util.mutation_type(wild_type_sequence.seq, mutant_sequence.seq),
            #"SEQUENCE_SIMILARITY": attributing_util.sequence_similarity(wild_type_sequence.seq, mutant_sequence.seq),
        }
    return mutation_bonding_factors


def exceute_all():
    # Predict effect of mutation
    data = util.read_text_data()
    for line in data[:2]:
        attributes = predict_mutation_effect(line["mutation"])

        # Output results
        results = {
            "VARIANT": line["mutation"],
            "ATTRIBUTES": attributes,
            "OBSERVATIONS": {
                "Severe": line["severe"],
                
            }
        }
        print(results)

def exceute(mutation):
    # Predict effect of mutation
    data = util.read_text_data()
    attributes = {}
    attributes = predict_mutation_effect(mutation)
    severe = ""
    for line in data:
        if line["mutation"] == mutation:
            severe = line["severe"]

    # Output results
    return {
        "VARIANT": line["mutation"],
        "ATTRIBUTES": attributes,
        "OBSERVATIONS": {
            "Severe": severe,
        }
    }

def get_mutations():
    data = util.read_text_data()
    return [line["mutation"] for line in data]
    
