import React from "react";

const TableRow = ({data: Data}) => {
  const indexingData = {
    // BINDING: [key, key2]
  };
  function roundUpTextValue(text) {
    // Convert the text to a number.
    const number = parseFloat(text);
  
    // If the number is not a number, return the original text.
    if (isNaN(number)) {
      return text;
    }
  
    // Round the number up to the nearest integer.
    const roundedNumber = number.toFixed(2);
  
    // Convert the rounded number back to a string.
    const roundedText = roundedNumber.toString();
  
    // Return the rounded text.
    return roundedText;
  }
  const processData = (data) => {
    Object.keys(data).forEach(key => {
      Object.keys(data[key]).forEach(attribute => {
        if (indexingData[attribute]) {
          indexingData[attribute].push(data[key][attribute]);
        } else {
          indexingData[attribute] = [data[key][attribute]];
        }
      });
    });
    Object.keys(indexingData).forEach(indexDataKey => {
      indexingData[indexDataKey].sort();
    });
    console.log(indexingData);
  };

  const getIndex = (key, value) => {
    return indexingData[key] ? 
      "index" + 
      indexingData[key].findIndex((a) => a === value): 
      '';
  }

  processData(Data);

  console.log(Data);

  return (
    <table className="table">
      <thead>
        <tr>
          <th>Neighbors</th>
          <th>DNA Affinity</th>
          {/*<th>Change Positions</th>*/}
          <th>Alignment Score</th>
          <th>Percentage Identity</th>
          <th>GC Content (Comparing - Mutation)</th>
          <th>Transition Traversion Ratio</th>
          <th>Genetic Distance</th>
          <th>Nucleotide Diversity</th>
          <th>Probable mutation</th>
        </tr>
      </thead>
        {console.log(Data)}
      {Object.keys(Data).map(key => {
        return (<tr>
          <td>{key.toUpperCase()}</td>
          <td className={getIndex("DNA BINDING_EFFECT", Data[key]["DNA BINDING_EFFECT"])}>{roundUpTextValue(Data[key]["DNA BINDING_EFFECT"])}</td>
          {/*<td className={getIndex("CHANGING_POSITIONS", Data[key]["CHANGING_POSITIONS"])}>{Data[key]["CHANGING_POSITIONS"]}</td>*/}
          <td className={getIndex("ALIGNMENT_SCORE", Data[key]["ALIGNMENT_SCORE"])}>{roundUpTextValue(Data[key]["ALIGNMENT_SCORE"])}</td>
          <td className={getIndex("PERCENTAGE_IDENTITY", Data[key]["PERCENTAGE_IDENTITY"])}>{roundUpTextValue(Data[key]["PERCENTAGE_IDENTITY"])}</td>
          <td className={getIndex("M_GC", Data[key]["M_GC"])}>{roundUpTextValue(Data[key]["M_GC"] - Data[key]["C_GC"])}</td>
          <td className={getIndex("TRANSITION_TRAVERSION_RATIO", Data[key]["TRANSITION_TRAVERSION_RATIO"])}>{roundUpTextValue(Data[key]["TRANSITION_TRAVERSION_RATIO"])}</td>
          <td className={getIndex("GENETIC_DISTANCE", Data[key]["GENETIC_DISTANCE"])}>{roundUpTextValue(Data[key]["GENETIC_DISTANCE"])}</td>
          <td className={getIndex("NUCLEOTIDE_DIVERSITY", Data[key]["NUCLEOTIDE_DIVERSITY"])}>{roundUpTextValue(Data[key]["NUCLEOTIDE_DIVERSITY"])}</td>
          <td className={getIndex("MUTATION_TYPE", Data[key]["MUTATION_TYPE"])}>{roundUpTextValue(Data[key]["MUTATION_TYPE"])}</td>
        </tr>
        );
      })}
    </table>
  );
};

export default TableRow;
