import { useOutletContext } from "react-router-dom";

function DyeResults() {
    const { dyeResults } = useOutletContext()

    return (
        <div>
            <h2>Dye Results</h2>
            <ul>
                {dyeResults.map((result) => (
                    <li>
                        <div>
                            <h3>Dye Material: {result.dye_material.name} + Mordant: {result.mordant.name}</h3>
                            <p>Resulting Color: {result.resulting_color}</p>
                            <p>Intensity: {result.intensity}</p>
                            <div>
                                <img src={result.dye_material.image} alt={result.dye_material.name} width={100} />
                                <img src={result.mordant.image} alt={result.mordant.name} width={100} />
                            </div>

                        </div>
                    </li>
                ))}
            </ul>

        </div>
    )
}

export default DyeResults;