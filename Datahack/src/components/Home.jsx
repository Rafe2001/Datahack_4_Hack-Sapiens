import React from 'react'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import FileUploads from './FileUploads'
import Translation from './Translation'
import { SidebarWithSearch } from './Sidebar'

const Home = () => {
  return (
    <div>
      <div className='text-3xl font-bold'>
        <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={2}>
            <Grid item xs={3} className='border-1px-solid'>
              <SidebarWithSearch />

            </Grid>
            <Grid item xs={8} className='border-10px-solid'>
              <FileUploads />
              <Translation />

            </Grid>

          </Grid>
        </Box>



      </div>
    </div>
  )
}

export default Home
// import * as React from 'react';
// import Stack from '@mui/material/Stack';
// import Button from '@mui/material/Button';

// export default function BasicButtons() {
//   return (
//     <Stack spacing={2} direction="row">
//       <Button variant="text">Text</Button>
//       <Button variant="contained">Contained</Button>
//       <Button variant="outlined">Outlined</Button>
//     </Stack>
//   );
// }