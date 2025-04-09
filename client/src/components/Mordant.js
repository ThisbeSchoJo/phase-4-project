function Mordant({ mordant }) {
  return (
    <li className="mordant">
      <h2>Mordant # {mordant.id}</h2>
      <h3>Name: {mordant.name}</h3>
      <p>
        RGB Effect: ({mordant.r_effect}, {mordant.g_effect}, {mordant.b_effect})
      </p>
      <img src={mordant.image} alt={mordant.name} />
    </li>
  );
}

export default Mordant;
