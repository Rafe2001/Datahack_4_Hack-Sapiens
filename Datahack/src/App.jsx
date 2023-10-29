import './App.css'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
// import { styled } from '@mui/material/styles';
import { SidebarWithSearch } from './components/Sidebar'
import Translation from './components/Translation';
import FileUploads from './components/FileUploads';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Document from './components/Document';
import Home from './components/Home';

function App() {

  return (
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
}

export default App
