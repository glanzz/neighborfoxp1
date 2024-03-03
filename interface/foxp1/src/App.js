import './App.css';
import TableRow from './TableRow';

var usage_data = {'VARIANT': 'c.532C>T p.(Gln178*)', 'ATTRIBUTES': {'il2': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 3780.0, 'PERCENTAGE_IDENTITY': 71.91780821917808, 'M_GC': 41.48061104582844, 'C_GC': 31.963470319634702, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.47280178837555886, 'GENETIC_DISTANCE': 0, 'NUCLEOTIDE_DIVERSITY': 0.7520928462709284, 'MUTATION_TYPE': 'Insertion'},'gatad2b': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 6808.0, 'PERCENTAGE_IDENTITY': 9.694553221787112, 'M_GC': 41.48061104582844, 'C_GC': 40.88430046279815, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.5050058892815077, 'GENETIC_DISTANCE': 0.1573098120181651, 'NUCLEOTIDE_DIVERSITY': 0.07278034887860449, 'MUTATION_TYPE': 'Deletion'}, 'foxp1': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 0, 'PERCENTAGE_IDENTITY': 0, 'M_GC': 41.48061104582844, 'C_GC': 41.1085208121779, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.4947776783049836, 'GENETIC_DISTANCE': 0.016048093593948935, 'NUCLEOTIDE_DIVERSITY': 0.007960004513158878, 'MUTATION_TYPE': 'Deletion'}, 'foxp4': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 6808.0, 'PERCENTAGE_IDENTITY': 12.156274551817727, 'M_GC': 41.48061104582844, 'C_GC': 54.7157345903864, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.5137395459976105, 'GENETIC_DISTANCE': 0.1996554105796209, 'NUCLEOTIDE_DIVERSITY': 0.09049353617598743, 'MUTATION_TYPE': 'Deletion'}, 'csf1r': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 6808.0, 'PERCENTAGE_IDENTITY': 11.333255647483812, 'M_GC': 41.48061104582844, 'C_GC': 48.09808393401142, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.511710643344204, 'GENETIC_DISTANCE': 0.1860474218130227, 'NUCLEOTIDE_DIVERSITY': 0.08488288858184481, 'MUTATION_TYPE': 'Deletion'}, 'blm': {'DNA BINDING_EFFECT': 21, 'CHANGING_POSITIONS': [], 'ALIGNMENT_SCORE': 6808.0, 'PERCENTAGE_IDENTITY': 6.88922395037492, 'M_GC': 41.48061104582844, 'C_GC': 40.73223302739296, 'M_HETEROZYGOSITY': 0.0, 'C_HETEROZYGOSITY': 0.0, 'TRANSITION_TRAVERSION_RATIO': 0.5054945054945055, 'GENETIC_DISTANCE': 0.1082419191002001, 'NUCLEOTIDE_DIVERSITY': 0.05129476528268283, 'MUTATION_TYPE': 'Deletion'}}, 'OBSERVATIONS': {'Severe': 'Mild'}}

function App() {
  const handleButtonOnClick = () => {
    const input = document.getElementById("search").value;
    // Send input to App
    console.log(input);
  };

  return (
    <div>
      <div className="header">
        <img className="logo" src="/logo.webp"/>
        <input id="search" placeholder="Enter Variant" type="search" minLength="3" />
        <button type="submit" onClick={handleButtonOnClick}>Submit</button>
      </div>
      <div className="content">
          <div>
            <div className="highlight">{usage_data["VARIANT"]}</div>
            <TableRow data={usage_data["ATTRIBUTES"]} />
          </div>
          <div className='flex'>
            <div>
              <h2>Related Conditions</h2>  
              <div>
                Severity: {usage_data['OBSERVATIONS']['Severe']}
              </div>
            </div>
            <div>
              <h2>Action Items</h2>
              <div>
                <ul>
                  <li>
                  Assess need for:
                    Community or online resources such as Parent to Parent;
                    Social work involvement for parental support;
                    Home nursing referral;
                    Early intervention referral;
                    Case management support referral.
                  </li>
                  <li>
                  To inform affected persons & their families re nature, MOI, & implications of FOXP1 syndrome to facilitate medical & personal decision making
                  </li>
                  <li>
                    To screen for behavior concerns incl ADHD, impulsivity, anxiety, sleep disturbances, &/or findings suggestive of ASD 1
                  </li>
                  <li>
                  Evaluate speech production & receptive/expressive language in all persons, regardless of age.
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
}

export default App;
