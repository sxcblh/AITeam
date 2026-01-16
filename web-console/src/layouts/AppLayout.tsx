import React from 'react'
import { Link, Outlet, useNavigate } from 'react-router-dom'
import { clearToken } from '../auth/token'

const navStyle: React.CSSProperties = {
  display: 'flex',
  gap: 12,
  padding: 12,
  borderBottom: '1px solid #eee',
  alignItems: 'center',
}

export function AppLayout() {
  const nav = useNavigate()

  return (
    <div>
      <div style={navStyle}>
        <strong>ALM Console</strong>
        <Link to="/">Dashboard</Link>
        <Link to="/projects">Projects</Link>
        <Link to="/requirements">Requirements</Link>
        <Link to="/bugs">Bugs</Link>
        <Link to="/releases">Releases</Link>
        <div style={{ marginLeft: 'auto' }}>
          <button
            onClick={() => {
              clearToken()
              nav('/login')
            }}
          >
            Logout
          </button>
        </div>
      </div>

      <div style={{ padding: 16 }}>
        <Outlet />
      </div>
    </div>
  )
}
