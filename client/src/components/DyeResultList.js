import { useOutletContext } from "react-router-dom"; 
import DyeResult from "./DyeResult"

function DyeResultList(){

    const { dyeResults } = useOutletContext()

    const dyeResultComponents = dyeResults.map(dyeResult => {
        return <DyeResult key={dyeResult.id} dyeResult={dyeResult}/>
    })

    return(
        <div>
            <h1>Here is the dye result list...</h1>
            <ul>{dyeResultComponents}</ul>
        </div>
    )
}

export default DyeResultList;