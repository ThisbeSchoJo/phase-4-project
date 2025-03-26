import { useOutletContext } from "react-router-dom";
import Volcano from "./Volcano"

function VolcanoList(){

    const {volcanoes} = useOutletContext()

    const volcanoComponents = volcanoes.map(volcano => {
        return <Volcano key={{volcano.id} volcano={volcano}}/>
    })

    return(
        <h1>Here is the volcano list...</h1>
    )
}

export default VolcanoList;