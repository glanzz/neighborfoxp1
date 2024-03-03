### Neighbor FoxP1 

#### Author: Bhargav C N, Hitesh K

- The tool models the given variant provided as input in HGVS format by reading the fasta of the existing FOXP1 and mutating upon it.
- The mutation sequence model is used further compare with the genes that have affiliation towards FOXP1
- Various quanitifiable attributes are derived between these models
- The derived attributes are presented to visualize alongside the limited dataset of severity associated with the FOXP1 variant and possible precautions to be taken. This approach allows us to map the limited dataset (which as a whole provides for lesser correlation) to abundant data of genes which are different and provide high correlation to understand the role it plays in treatement of rare disease.



### Internal Working
The working of the model involves three major steps:
- Model the mutation of the gene using the input provided in HVGS format
- Load all the models of genes that interact with FOXP1
- Generate attributes which count for the correlation between the genes


### Usage
Note: Requires python >=3.12 
- Install requirements<pre>pip install -r requirements.txt</pre>
- The application is configured to use as both API and commandline tool
  Use command to run the local server and access API <pre>flask run</pre>
- Use command line by the following command
  <pre> flask generate --genes gatad2b,il2 --name c.532C>T p.(Gln178*)</pre>
  The genes are genes that foxp1 interact with and name is the HGVS format representation of FOXP1 mutation
  <br/>
- Use the visual tool by running
  <pre>
    cd app/interface/foxp1
    npm start
  </pre>



