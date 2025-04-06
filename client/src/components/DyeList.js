import { useOutletContext } from "react-router-dom"; 
import DyeMaterial from "./DyeMaterial"

function DyeList(){

    const { dyeMaterials } = useOutletContext()

    const dyeMaterialComponents = dyeMaterials.map(dyeMaterial => {
        return <DyeMaterial key={dyeMaterial.id} dyeMaterial={dyeMaterial}/>
    })

    return(
        <div>
            <h1>Here is the dye list...</h1>
            <ul>{dyeMaterialComponents}</ul>
        </div>
    )
}

export default DyeList;