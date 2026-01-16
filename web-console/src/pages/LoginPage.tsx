import React, { useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { login } from '../api/client'
import { setToken } from '../auth/token'

export default function LoginPage() {
  const nav = useNavigate()
  const loc = useLocation() as any
  const [username, setUsername] = useState('admin')
  const [password, setPassword] = useState('admin123')
  const [error, setError] = useState('')

  const from = loc.state?.from?.pathname || '/'

  return (
    <div style={{ maxWidth: 360, margin: '100px auto', border: '1px solid #eee', padding: 16 }}>
      <h2>Login</h2>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        <input placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input placeholder="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

        {error ? <div style={{ color: 'crimson' }}>{error}</div> : null}

        <button
          onClick={async () => {
            setError('')
            try {
              const data = await login(username, password)
              setToken(data.access_token)
              nav(from, { replace: true })
            } catch (e: any) {
              setError(e?.response?.data?.detail || 'Login failed')
            }
          }}
        >
          Sign In
        </button>

        <div style={{ fontSize: 12, color: '#666' }}>
          dev demo accounts: admin/admin123, dev/dev123
        </div>
      </div>
    </div>
  )
}
