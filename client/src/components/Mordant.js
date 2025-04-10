function Mordant({ mordant }) {
  return (
    <div className="mordant-card">
      <h3>{mordant.name}</h3>
      <p>
        RGB Effect: ({mordant.r_effect}, {mordant.g_effect}, {mordant.b_effect})
      </p>
      <div className="image-container">
        <img src={mordant.image} alt={mordant.name} />
      </div>
    </div>
  );
}

export default Mordant;
