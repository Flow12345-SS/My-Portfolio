// frontend/src/pages/AdminDashboard.jsx
import React, { useEffect, useState } from "react";
import { fetchProjects, createProject, updateProject, deleteProject } from "../api";
import ProjectForm from "../components/ProjectForm";

export default function AdminDashboard(){
  const [projects, setProjects] = useState([]);
  const [editing, setEditing] = useState(null);
  const token = localStorage.getItem("token");

  const load = () => fetchProjects().then(setProjects).catch(console.error);

  useEffect(()=>{ load(); }, []);

  const onCreate = async (form) => {
    try{
      await createProject(form, token);
      await load();
    }catch(e){ console.error(e); alert("Create failed"); }
  };

  const onUpdate = async (id, form) => {
    try{
      await updateProject(id, form, token);
      setEditing(null);
      await load();
    }catch(e){ console.error(e); alert("Update failed"); }
  };

  const onDelete = async (id) => {
    if(!confirm("Delete?")) return;
    try{
      await deleteProject(id, token);
      await load();
    }catch(e){ console.error(e); alert("Delete failed"); }
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Admin Dashboard</h1>
      <div className="mb-6">
        <h2 className="font-semibold mb-2">Create New Project</h2>
        <ProjectForm onSubmit={onCreate} />
      </div>

      <h2 className="font-semibold mb-2">Projects</h2>
      <div className="space-y-3">
        {projects.map(p => (
          <div key={p.id} className="border p-3 rounded">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-semibold">{p.title}</h3>
                <p className="text-sm">{p.description}</p>
              </div>
              <div className="space-x-2">
                <button className="px-2 py-1 bg-yellow-300 rounded" onClick={()=>setEditing(p)}>Edit</button>
                <button className="px-2 py-1 bg-red-500 text-white rounded" onClick={()=>onDelete(p.id)}>Delete</button>
              </div>
            </div>
            {editing && editing.id === p.id && (
              <div className="mt-3">
                <ProjectForm initial={editing} onSubmit={(form)=>onUpdate(p.id, form)} onCancel={()=>setEditing(null)} />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
