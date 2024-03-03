import requests
import os
import subprocess
from Bio.PDB import PDBParser, Superimposer
from itertools import product
from Bio.SeqUtils import nt_search


def get_motifs():
    # Define the consensus binding motif for FOXP1
    consensus_motif = "RYMAAYA"

    # Define the possible nucleotides at each position
    possible_nucleotides = {
        "R": ["A", "G"],
        "Y": ["C", "T"],
        "M": ["A", "C"]
    }

    # Generate all possible combinations of nucleotides
    all_possible_motifs = [''.join(p) for p in product(*[possible_nucleotides.get(base, [base]) for base in consensus_motif])]

    # Print the list of all possible binding motifs for FOXP1

    return all_possible_motifs

def get_structure(protien_id):
    pdb_path = retrieve_structure_from_pdb(protein_id=protien_id)
    pdb_parser = PDBParser()
    return pdb_parser.get_structure(protien_id, pdb_path)

# Function to mutate a residue in the protein structure
def mutate_residue(structure, chain_id, position, mutant_residue):
    # Iterate over all residues in the structure
    for model in structure:
        for chain in model:
            if chain.id == chain_id:
                for residue in chain:
                    # Check if the residue index matches the specified position
                    if residue.id[1] == position:
                        # Modify the residue to the mutant residue
                        residue.resname = mutant_residue
    
    return structure

# Function to retrieve protein structure from PDB
def retrieve_structure_from_pdb(protein_id):
    # Download PDB file for the given protein ID
    pdb_file = f"{protein_id}.pdb"
    if not os.path.exists(pdb_file):
        subprocess.run(["curl", "-O", f"https://files.rcsb.org/download/{protein_id}.pdb"])
    
    # Return the path to the downloaded PDB file
    return pdb_file

# Function to calculate solvent accessibility change using DSSP
def calculate_solvent_accessibility_change(pdb_file):
    # Run DSSP to calculate solvent accessibility
    dssp_output = subprocess.check_output(["dssp", "-i", pdb_file])
    
    # Parse DSSP output to extract solvent accessibility information
    # Calculate the change in solvent accessibility for the mutated residue
    # (you can use Biopython's DSSP module for parsing)
    solvent_accessibility_change = 0.0  # Placeholder for solvent accessibility change
    
    return solvent_accessibility_change

# Function to predict residue contacts effect using PSICOV
def predict_residue_contacts_effect(pdb_file):
    # Run PSICOV to predict residue contacts
    psicov_output = subprocess.check_output(["psicov", pdb_file])
    
    # Parse PSICOV output to extract residue contact predictions
    # Analyze the change in contacts involving the mutated residue
    # (you may need to parse the output and compare contacts involving the wild type and mutant residues)
    residue_contacts_effect = 0.0  # Placeholder for residue contacts effect
    
    return residue_contacts_effect

# Function to calculate RMSD between two protein structures
def calculate_rmsd(structure1, structure2):
    super_imposer = Superimposer()
    atoms1 = []
    atoms2 = []

    for model1, model2 in zip(structure1, structure2):
        for chain1, chain2 in zip(model1, model2):
            atoms1 += [atom for atom in chain1.get_atoms()]
            atoms2 += [atom for atom in chain2.get_atoms()]

    super_imposer.set_atoms(atoms1, atoms2)
    rmsd = super_imposer.rms

    return rmsd

def get_binding_affinity(wild_type_sequence, mutant_sequence, binding_motif):
    wild_type_motif_position = nt_search(str(wild_type_sequence), binding_motif)
    mutant_motif_position = nt_search(str(mutant_sequence), binding_motif)

    # Calculate the binding affinity based on motif position
    wild_type_binding_affinity = len(wild_type_motif_position)
    mutant_binding_affinity = len(mutant_motif_position)

    

    return mutant_binding_affinity

# Function to predict effect on DNA binding, dimerization, and interaction with other transcription factors
def predict_functional_effects(wild_type_residue, mutant_residue):
    # Placeholder for functional effect prediction
    dna_binding_effect = 0.0
    dimerization_effect = 0.0
    interaction_effect = 0.0
    
    # Implement prediction algorithms or use available tools to predict functional effects
    
    return dna_binding_effect, dimerization_effect, interaction_effect



def read_text_data(file="app/Dataset.txt"):
    data = []
    with open(file, "r") as f:
        f.readline()
        for line in f.readlines():
            tokens = line.split(",")
            data.append({"severe": tokens[0], "mutation": tokens[1]})
    return data


def get_swiss_pdb_id(amino_acid_sequence):

    # SWISS-MODEL API endpoint
    url = "https://swissmodel.expasy.org/repository/uniprot/" + amino_acid_sequence + ".json"

    # Request protein structure prediction
    response = requests.get(url)

    if response.status_code == 200:
        # Extract the PDB ID of the predicted structure
        response = response.json()
        print(response)
        pdb_id = response['result']['structures'][0]['pdbId']
        return pdb_id
    else:
        print(response.status_code)
        print("Failed to retrieve protein structure prediction.")

def get_phyre2_pdb(amino_acid_sequence):
    url = "http://www.sbg.bio.ic.ac.uk/phyre2/webservices/rest/result/"

    # Parameters for the API request
    params = {
        "seq": amino_acid_sequence,
        "outfmt": "json"
    }

    # Request protein structure prediction
    response = requests.post(url, data=params)

    if response.status_code == 200:
        # Extract the PDB ID of the predicted structure
        response = response.json()
        print(response)
        pdb_id = response['data']['pdb']
        print("Predicted PDB ID:", pdb_id)
    else:
        print("Failed to retrieve protein structure prediction.")
    
def get_robetta(amino_acid_sequence):
    url = "https://robetta.bakerlab.org/submit"

    # Parameters for the API request
    params = {
        "sequence": amino_acid_sequence,
        "json": "true"
    }

    # Request protein structure prediction
    response = requests.post(url, data=params)

    if response.status_code == 200:
        # Extract the PDB ID of the predicted structure
        pdb_id = response.json()['id']
        print("Predicted PDB ID:", pdb_id)
    else:
        print(response.status_code)
        print("Failed to retrieve protein structure prediction.")
