function DyeResult({dyeResult}) {
    return (
        <li>
            <h2>Dye Result # {dyeResult.id} </h2>
            <h3>Dye Material: {dyeResult.dye_material.name} + Mordant: {dyeResult.mordant.name}</h3>
            <p>Resulting Color: {dyeResult.resulting_color}</p>
            <p>Intensity: {dyeResult.intensity}</p>
            <div>
                <img src={dyeResult.dye_material.image} alt={dyeResult.dye_material.name} width={100} />
                <img src={dyeResult.mordant.image} alt={dyeResult.mordant.name} width={100} />
                {/* SHOULD ADD IN BOX THAT IS THE RESULTING COLOR */}
             </div>            
        </li>
    )}

export default DyeResult;