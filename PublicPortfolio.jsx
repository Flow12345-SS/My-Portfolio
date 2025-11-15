// frontend/src/pages/PublicPortfolio.jsx
import React, { useEffect, useState } from "react";
import { fetchProjects } from "../api";

export default function PublicPortfolio() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects().then(setProjects).catch(console.error);
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">My Portfolio</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {projects.map((p) => (
          <div key={p.id} className="border p-4 rounded shadow">
            {p.image_filename && (
              <img src={`${import.meta.env.VITE_API_BASE || "http://localhost:8000"}/static/uploads/${p.image_filename}`} alt={p.title} className="w-full h-40 object-cover mb-2 rounded" />
            )}
            <h2 className="text-xl font-semibold">{p.title}</h2>
            <p className="text-sm">{p.description}</p>
            {p.tech_stack && <p className="text-xs mt-1">Tech: {p.tech_stack}</p>}
            {p.link && (
              <a href={p.link} target="_blank" rel="noreferrer" className="text-blue-600 text-sm">
                View Project
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
