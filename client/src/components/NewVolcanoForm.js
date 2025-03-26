import { useOutletContext } from "react-router-dom";
import { useState } from "react";

 function NewVolcanoForm(){

    const { addVolcano } = useOutletContext()

    const navigate = useNavigate()

    const [formData, setFormData] = useState({
        location: "",
        image: ""
    })

    function handleSubmit(event){
        event.preventDefault()
        fetch('/volcanoes', {
            method: "POST",
            headders: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(formData)
            })
            .then(response.ok){
                response.json().then(newVolcanoData => {
                    addVolcano(newVolcanoData)
                    navigate('/')
                })
            }
            else{
                response.json().then(errorObject => {
                    alert(`Error: ${errorObject.error}`)
                })
            }
    }

    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }

    return (
        <div>
            <h2>New Volcano Form</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="new-location">Location: </label>
                <input onChange={updateFormData} type="text" id="new-location" name="location" value={formData.location}/>
                <label htmlFor="new-image">Image: </label>
                <input onChange={updateFormData} type="text" id="new-image" name="image" value={formData.image}/>
                <br/><br/>
                <input type="submit" value="Add Volcano"/>
            </form>
        </div>
    )
 }

 export default NewVolcanoForm