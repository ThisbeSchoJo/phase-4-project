import { useOutletContext } from "react-router-dom";
import DyeResult from "./DyeResult";

function DyeResultList() {
  const { dyeResults } = useOutletContext();

  // Add console logging to help diagnose the issue
  console.log("DyeResults from context:", dyeResults);

  if (!dyeResults) {
    return <div>Loading dye results...</div>;
  }

  if (dyeResults.length === 0) {
    return <div>No dye results found.</div>;
  }

  const dyeResultComponents = dyeResults.map((dyeResult) => {
    // Add console logging for each dyeResult
    console.log("Processing dyeResult:", dyeResult);

    if (!dyeResult) {
      console.error("Found undefined dyeResult in the array");
      return null;
    }

    return <DyeResult key={dyeResult.id} dyeResult={dyeResult} />;
  });

  return (
    <div>
      <h1>Here is the dye result list...</h1>
      <div className="dye-result-grid">{dyeResultComponents}</div>
    </div>
  );
}

export default DyeResultList;
