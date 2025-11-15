// frontend/src/api.js
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export const api = axios.create({
  baseURL: API_BASE,
});

export async function login(username, password) {
  const params = new URLSearchParams();
  params.append("username", username);
  params.append("password", password);
  const resp = await api.post("/auth/token", params);
  return resp.data; // { access_token, token_type }
}

export async function fetchProjects() {
  const resp = await api.get("/projects/");
  return resp.data;
}

export async function createProject(formData, token) {
  const resp = await api.post("/projects/", formData, {
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "multipart/form-data" },
  });
  return resp.data;
}

export async function updateProject(id, formData, token) {
  const resp = await api.put(`/projects/${id}`, formData, {
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "multipart/form-data" },
  });
  return resp.data;
}

export async function deleteProject(id, token) {
  const resp = await api.delete(`/projects/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return resp.data;
}
