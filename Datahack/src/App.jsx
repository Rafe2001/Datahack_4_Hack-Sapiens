import './App.css';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { SidebarWithSearch } from './components/Sidebar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <div className='text-3xl font-bold'>
            <Box sx={{ flexGrow: 1 }}>
              <Grid container spacing={2}>
                <Grid item xs={4} className='border-1px-solid'>
                  <SidebarWithSearch />
                </Grid>
                <Grid item xs={8} className='border-10px-solid'>
                  hi ernvewjbvj
                </Grid>
              </Grid>
            </Box>
          </div>
        } />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
