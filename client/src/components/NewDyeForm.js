

function NewDyeForm(){
    return(
        <div>
            <h2>Add a new dye!</h2>
            <form>
                <label htmlFor="new-dye">Dye Material: </label>
                <input type="text" id="new-dye" name="dye"/>
                <br></br>
                <br></br>
                <label htmlFor="new-base-color">Base Color: </label>
                <input type="text" id="new-base-color" name="base-color"/>
                <br></br>
                <br></br>
                <label htmlFor="new-image">Image URL: </label>
                <input type="text" id="new-image" name="image" />
                <br></br>
                <br></br>
                <input type="submit" value="Add Dye"/>
            </form>
        </div>
    )
}

export default NewDyeForm;