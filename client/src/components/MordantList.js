import { useOutletContext } from "react-router-dom"; 
import Mordant from "./Mordant"

function MordantList(){

    const { mordants } = useOutletContext()

    const mordantComponents = mordants.map(mordant => {
        return <Mordant key={mordant.id} mordant={mordant}/>
    })

    return(
        <div>
            <h1>Here is the mordant list...</h1>
            <ul>{mordantComponents}</ul>
        </div>
    )
}

export default MordantList;