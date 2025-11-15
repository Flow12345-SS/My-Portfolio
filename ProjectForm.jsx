// frontend/src/components/ProjectForm.jsx
import React, { useState } from "react";

export default function ProjectForm({ initial = null, onSubmit, onCancel }){
  const [title, setTitle] = useState(initial?.title || "");
  const [description, setDescription] = useState(initial?.description || "");
  const [tech, setTech] = useState(initial?.tech_stack || "");
  const [link, setLink] = useState(initial?.link || "");
  const [featured, setFeatured] = useState(initial?.featured || false);
  const [image, setImage] = useState(null);

  const handle = (e) => {
    e.preventDefault();
    const fd = new FormData();
    fd.append("title", title);
    fd.append("description", description);
    fd.append("tech_stack", tech);
    fd.append("link", link);
    fd.append("featured", featured ? "true" : "false");
    if(image) fd.append("image", image);
    onSubmit(fd);
  };

  return (
    <form onSubmit={handle} className="flex flex-col gap-2 border p-3 rounded">
      <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="Title" required className="border p-2 rounded" />
      <textarea value={description} onChange={e=>setDescription(e.target.value)} placeholder="Description" className="border p-2 rounded" />
      <input value={tech} onChange={e=>setTech(e.target.value)} placeholder="Tech stack (comma separated)" className="border p-2 rounded" />
      <input value={link} onChange={e=>setLink(e.target.value)} placeholder="Project link" className="border p-2 rounded" />
      <label className="flex items-center gap-2">
        <input type="checkbox" checked={featured} onChange={e=>setFeatured(e.target.checked)} />
        Featured
      </label>
      <input type="file" onChange={e=>setImage(e.target.files?.[0]||null)} />
      <div className="flex gap-2">
        <button className="bg-blue-600 text-white px-3 py-1 rounded">Save</button>
        {onCancel && <button type="button" onClick={onCancel} className="px-3 py-1 rounded border">Cancel</button>}
      </div>
    </form>
  );
}
