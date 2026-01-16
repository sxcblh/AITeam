import React from 'react'
import { Route, Routes, Navigate } from 'react-router-dom'

import { RequireAuth } from './auth/RequireAuth'
import { AppLayout } from './layouts/AppLayout'

import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import ProjectsPage from './pages/ProjectsPage'
import RequirementsPage from './pages/RequirementsPage'
import BugsPage from './pages/BugsPage'
import ReleasesPage from './pages/ReleasesPage'

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />

      <Route
        path="/"
        element={
          <RequireAuth>
            <AppLayout />
          </RequireAuth>
        }
      >
        <Route index element={<DashboardPage />} />
        <Route path="projects" element={<ProjectsPage />} />
        <Route path="requirements" element={<RequirementsPage />} />
        <Route path="bugs" element={<BugsPage />} />
        <Route path="releases" element={<ReleasesPage />} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
