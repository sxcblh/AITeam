import React, { useEffect, useState } from 'react'
import { listReleases } from '../api/client'

export default function ReleasesPage() {
  const [rows, setRows] = useState<any[]>([])

  useEffect(() => {
    ;(async () => {
      const data = await listReleases()
      setRows(data)
    })()
  }, [])

  return (
    <div>
      <h2>Releases</h2>
      <p style={{ color: '#666' }}>MVP 只做列表展示，后续加：Release Notes、审批流、发布记录。</p>

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>ID</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Version</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Status</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Build No</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              <td style={{ padding: 6 }}>{r.id}</td>
              <td style={{ padding: 6 }}>{r.version}</td>
              <td style={{ padding: 6 }}>{r.status}</td>
              <td style={{ padding: 6 }}>{r.build_no}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
