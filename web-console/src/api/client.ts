import { http } from './http'

export async function login(username: string, password: string) {
  const res = await http.post('/auth/login', { username, password })
  return res.data as { access_token: string; token_type: string }
}

export async function listProjects() {
  const res = await http.get('/projects')
  return res.data as any[]
}

export async function createProject(payload: { key: string; name: string; description?: string }) {
  const res = await http.post('/projects', payload)
  return res.data
}

export async function listRequirements(project_id?: number) {
  const res = await http.get('/requirements', { params: { project_id } })
  return res.data as any[]
}

export async function listBugs(project_id?: number) {
  const res = await http.get('/bugs', { params: { project_id } })
  return res.data as any[]
}

export async function listReleases(project_id?: number) {
  const res = await http.get('/releases', { params: { project_id } })
  return res.data as any[]
}
