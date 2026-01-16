import React, { useEffect, useState } from 'react'
import { listRequirements } from '../api/client'

export default function RequirementsPage() {
  const [rows, setRows] = useState<any[]>([])

  useEffect(() => {
    ;(async () => {
      const data = await listRequirements()
      setRows(data)
    })()
  }, [])

  return (
    <div>
      <h2>Requirements</h2>
      <p style={{ color: '#666' }}>MVP 只做列表展示，后续加：新建/编辑/状态流转/验收标准。</p>

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>ID</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Title</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Status</th>
            <th style={{ textAlign: 'left', borderBottom: '1px solid #eee' }}>Assignee</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              <td style={{ padding: 6 }}>{r.id}</td>
              <td style={{ padding: 6 }}>{r.title}</td>
              <td style={{ padding: 6 }}>{r.status}</td>
              <td style={{ padding: 6 }}>{r.assignee}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
