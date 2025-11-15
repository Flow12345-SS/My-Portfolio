// frontend/src/pages/AdminLogin.jsx
import React, { useState } from "react";
import { login } from "../api";
import { useNavigate } from "react-router-dom";

export default function AdminLogin(){
  const [u,setU]=useState(""); const [p,setP]=useState("");
  const nav = useNavigate();
  const onSubmit = async (e) => {
    e.preventDefault();
    try{
      const data = await login(u,p);
      localStorage.setItem("token", data.access_token);
      nav("/admin");
    }catch(err){
      alert("Login failed");
    }
  };
  return (
    <div className="p-6 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Admin Login</h1>
      <form onSubmit={onSubmit} className="flex flex-col gap-3">
        <input value={u} onChange={e=>setU(e.target.value)} required placeholder="username" className="border p-2 rounded" />
        <input type="password" value={p} onChange={e=>setP(e.target.value)} required placeholder="password" className="border p-2 rounded" />
        <button className="bg-blue-600 text-white p-2 rounded">Login</button>
      </form>
    </div>
  );
}
