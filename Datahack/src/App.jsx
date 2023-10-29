import './App.css';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
<<<<<<< HEAD
// import { styled } from '@mui/material/styles';
import { SidebarWithSearch } from './components/Sidebar'
import Translation from './components/Translation';
import FileUploads from './components/FileUploads';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Document from './components/Document';
import Home from './components/Home';
=======
import { SidebarWithSearch } from './components/Sidebar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
>>>>>>> 3ca37303349d5ae8af809f718b061a79fd772c32

function App() {
  return (
<<<<<<< HEAD
    <>
    <Router>
        <Routes>
          <Route path="/document" element={<Document/>} />
          <Route path="/translation" element={<Translation />} />
          <Route path="/" element={<Home />} />
          
       

  

      </Routes>
      </Router>

    </>
  )
=======
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
>>>>>>> 3ca37303349d5ae8af809f718b061a79fd772c32
}

export default App;
