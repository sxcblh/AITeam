import React, { useEffect, useState } from 'react'
import { listBugs } from '../api/client'

export default function BugsPage() {
  const [rows, setRows] = useState<any[]>([])

  useEffect(() => {
    ;(async () => {
      const data = await listBugs()
      setRows(data)
    })()
  }, [])

  return (
    <div>
      <h2>Bugs</h2>
      <p style={{ color: '#666' }}>MVP 只做列表展示，后续加：严重等级、复现步骤、回归记录。</p>

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>ID</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Title</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Status</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Severity</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              <td style={{ padding: 6 }}>{r.id}</td>
              <td style={{ padding: 6 }}>{r.title}</td>
              <td style={{ padding: 6 }}>{r.status}</td>
              <td style={{ padding: 6 }}>{r.severity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
