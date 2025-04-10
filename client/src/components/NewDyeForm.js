import { useOutletContext, useNavigate } from "react-router-dom";
import { useState } from "react";

function NewDyeForm(){
    const { addDyeMaterial } = useOutletContext()
    const navigate = useNavigate()

    const [formData, setFormData] = useState({
        name: "",
        r: "",
        g: "",
        b: "",
        image: ""
    })

    function handleSubmit(event) {

        console.log("Submitting form with:", formData); // Debugging output


        event.preventDefault();

        fetch('/dye_materials', {
            method: 'POST',
            headers: {
                "Content-Type" : "application/json",
                "Accept" : "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (response.ok) {
                response.json().then(newDyeData => {
                    addDyeMaterial(newDyeData) //Add the new dye material to the state

                    setFormData({
                        name: "",
                        r: "",
                        g: "",
                        b: "",
                        image: ""
                    })

                    navigate('/') //redict to home page
                })
            } else {
                response.json().then(errorObject => {
                    alert(`Error: ${errorObject.error}`)
                })
            }
        })
    }

    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }


    return(
        <div>
            <h2>Add a new dye!</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="new-dye">Dye Material: </label>
                <input onChange={updateFormData} type="text" id="new-dye" name="name" value={formData.name}/>
                <br></br>
                <br></br>
                <label htmlFor="new-r">Red: </label>
                <input onChange={updateFormData} type="number" id="new-r" name="r" value={formData.r}/>
                <br></br>
                <br></br>
                <label htmlFor="new-g">Green: </label>
                <input onChange={updateFormData} type="number" id="new-g" name="g" value={formData.g}/>
                <br></br>
                <br></br>
                <label htmlFor="new-b">Blue: </label>
                <input onChange={updateFormData} type="number" id="new-b" name="b" value={formData.b}/>
                <br></br>
                <br></br>
                <label htmlFor="new-image">Image URL: </label>
                <input onChange={updateFormData} type="text" id="new-image" name="image" value={formData.image}/>
                <br></br>
                <br></br>
                <input type="submit" value="Add Dye"/>
            </form>
        </div>
    )
}

export default NewDyeForm;