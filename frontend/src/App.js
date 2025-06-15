import React, { useEffect, useState } from 'react';

function App() {
  const [mensaje, setMensaje] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/hello')
      .then(res => res.json())
      .then(data => setMensaje(data.message))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>PowerUp ⚡</h1>
      <p>{mensaje}</p>
    </div>
  );
}

export default App;
