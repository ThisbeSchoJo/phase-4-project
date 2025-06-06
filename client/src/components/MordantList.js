import { useOutletContext } from "react-router-dom";
import Mordant from "./Mordant";

function MordantList() {
  const { mordants } = useOutletContext();

  if (!mordants) {
    return <div>Loading mordants...</div>;
  }

  const mordantComponents = mordants.map((mordant) => {
    return <Mordant key={mordant.id} mordant={mordant} />;
  });

  return (
    <div>
      {/* <h1>Here is the mordant list...</h1> */}
      <div className="mordant-grid">{mordantComponents}</div>
    </div>
  );
}

export default MordantList;
