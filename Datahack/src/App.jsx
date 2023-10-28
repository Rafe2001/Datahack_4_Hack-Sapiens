import './App.css'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { styled } from '@mui/material/styles';
import { SidebarWithSearch } from './components/Sidebar'

function App() {

  return (
    <>

      <div className='text-3xl font-bold'>
      <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>
        <Grid item xs={4} className='border-1px-solid'>
        <SidebarWithSearch />

        </Grid>
        <Grid item xs={8}  className='border-10px-solid'>
          hi
          ernvewjbvj
        </Grid>
          {/* <Grid item xs={4}>
            hi
          </Grid>
          <Grid item xs={8}>
            hi
          </Grid> */}
      </Grid>
    </Box>
       
        
      </div>



    </>
  )
}

export default App
