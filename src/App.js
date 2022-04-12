import './App.css';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Chip from '@mui/material/Chip';
import React from 'react';

function App() 
{
  const [HW1Field, setHW1Field] = React.useState(0)
  const [HW2Field, setHW2Field] = React.useState(0)
  const [HW1Out, setHW1Out] = React.useState(0);
  const [HW2Out, setHW2Out] = React.useState(0);
  const maxHW1 = 100;
  const maxHW2 = 200;

  return (
    <div className='checkout'>
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
      />
      <Grid container spacing={2}>
        <Grid item xs={3}>
          <Typography variant="overline">
            HWSet 1
            <br />
            Capacity: {maxHW1}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <TextField id="HW1_Input" label="" variant="outlined" onChange={(event) => setHW1Field(event.target.value)}/>
        </Grid>
        <Grid item xs={3}>
          <Chip id="HW1_Display" label={HW1Out + " units checked out."} variant="outlined" />
        </Grid>
        <Grid item xs={3}>
          <Button variant="contained" onClick={() => 
          {
            fetch("http://localhost:5000/hardware", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "qty" : HW1Field,
                "proj" : "project 1",
                "hwset" : "1"
              })
            })
              .then((res) => res.json())
              .then((data) => {
                if (data.success) {
                  alert("Successfully checked out.");
                  setHW1Out(data.amount)
                }
              })
              console.log(HW1Field)
            }}>
            Check Out
          </Button>
        </Grid>
      </Grid>

      <div className='divider' />

      <Grid container spacing={2}>
        <Grid item xs={3}>
          <Typography variant="overline">
            HWSet 2
            <br />
            Capacity: {maxHW2}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <TextField id="HW2_Input" label="" variant="outlined" onChange={(event) => setHW2Field(event.target.value)} />
        </Grid>
        <Grid item xs={3}>
          <Chip id="HW2_Display" label={HW2Out + " units checked out."} variant="outlined" />
        </Grid>
        <Grid item xs={3}>
        <Button variant="contained" onClick={() => 
          {
            fetch("http://localhost:5000/hardware", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "qty" : HW2Field,
                "proj" : "project 1",
                "hwset" : "2"
              })
            })
              .then((res) => res.json())
              .then((data) => {
                if (data.success) {
                  alert("Successfully checked out.");
                  setHW2Out(data.amount)
                }
              })
            }}>
            Check Out
          </Button>
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
