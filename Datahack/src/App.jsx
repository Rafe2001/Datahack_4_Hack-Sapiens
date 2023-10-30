import './App.css';
// import Grid from '@mui/material/Grid';
  // import Box from '@mui/material/Box';
// import { styled } from '@mui/material/styles';
// import { SidebarWithSearch } from './components/Sidebar'
import Translation from './components/Translation';
// import FileUploads from './components/FileUploads';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Document from './components/Document';
import Home from './components/Home';
// import { SidebarWithSearch } from './components/Sidebar';
// import Login from './components/Login';

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
  //   <BrowserRouter>
  //     <Routes>
  //       <Route path="/" element={
  //         <div className='text-3xl font-bold'>
  //           <Box sx={{ flexGrow: 1 }}>
  //             <Grid container spacing={2}>
  //               <Grid item xs={4} className='border-1px-solid'>
  //                 <SidebarWithSearch />
  //               </Grid>
  //               <Grid item xs={8} className='border-10px-solid'>
  //                 hi ernvewjbvj
  //               </Grid>
  //             </Grid>
  //           </Box>
  //         </div>
  //       } />
  //       <Route path="/login" element={<Login />} />
  //     </Routes>
  //   </BrowserRouter>
  // );
}

export default App;
