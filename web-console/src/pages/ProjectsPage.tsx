import React, { useEffect, useState } from 'react'
import { createProject, listProjects } from '../api/client'

export default function ProjectsPage() {
  const [rows, setRows] = useState<any[]>([])
  const [key, setKey] = useState('demo')
  const [name, setName] = useState('Demo Project')

  async function refresh() {
    const data = await listProjects()
    setRows(data)
  }

  useEffect(() => {
    refresh()
  }, [])

  return (
    <div>
      <h2>Projects</h2>

      <div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
        <input value={key} onChange={(e) => setKey(e.target.value)} placeholder="key" />
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="name" />
        <button
          onClick={async () => {
            await createProject({ key, name })
            await refresh()
          }}
        >
          Create
        </button>
      </div>

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>ID</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Key</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Name</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              <td style={{ padding: 6 }}>{r.id}</td>
              <td style={{ padding: 6 }}>{r.key}</td>
              <td style={{ padding: 6 }}>{r.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
