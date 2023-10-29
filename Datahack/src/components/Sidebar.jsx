import React from "react";
  // import { Link } from 'react-router-dom';
import {
  Card,
  Typography,
  List,
  ListItem,
  ListItemPrefix,
  ListItemSuffix,
  Chip,
  Accordion,
  AccordionHeader,
  AccordionBody,
  Alert,
  Input,
} from "@material-tailwind/react";
import {
  PresentationChartBarIcon,
  ShoppingBagIcon,
  UserCircleIcon,
  Cog6ToothIcon,
  InboxIcon,
  PowerIcon,
} from "@heroicons/react/24/solid";
import {
  ChevronRightIcon,
  ChevronDownIcon,
  CubeTransparentIcon,
  MagnifyingGlassIcon,
} from "@heroicons/react/24/outline";

export function SidebarWithSearch() {
  const [open, setOpen] = React.useState(0);
  const [openAlert, setOpenAlert] = React.useState(true);
  const [darkMode, setDarkMode] = React.useState(false);



  // const toggleDarkMode = () => {
  //   setDarkMode(!darkMode);
  // };

  // const handleOpen = (value) => {
  //   setOpen(open === value ? 0 : value);
  // };


  return (
    <div className={`h-screen flex ${darkMode ? "dark" : ""}`}>
      <div className={`bg-white dark:bg-gray-900 transition-all flex-1`}>
        <Card className="h-[calc(100vh-2rem)] w-full max-w-[20rem] p-4 shadow-xl shadow-blue-gray-900/5">
          <div className="mb-2 flex items-center gap-4 p-4">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvByh8ExhBokqH6PbFN_GYlYgHRtbRk-qVpw&usqp=CAU" alt="brand" className="h-8 w-8" />
            <Typography variant="h5" color="blue-gray">
              Hack-Sapiens
            </Typography>
          </div>
          <div className="p-2">
            <Input icon={<MagnifyingGlassIcon className="h-5 w-5 " />} label="Search" />
          </div>
          <List>
            {/* <Link to="/translation"> */}
              <ListItem className="pt-10">
                <ListItemPrefix>
                  <InboxIcon className="h-5 w-5" />
                </ListItemPrefix>
                {/* <Link to="/translation">Translation</Link> */}
                Translation
                <ListItemSuffix>
                  <Chip value="14" size="sm" variant="ghost" color="blue-gray" className="rounded-full" />
                </ListItemSuffix>
              </ListItem>
            {/* </Link> */}
            <ListItem>
              <ListItemPrefix>
                <UserCircleIcon className="h-5 w-5" />
              </ListItemPrefix>
              Summary
            </ListItem>
            <ListItem>
              <ListItemPrefix>
                <Cog6ToothIcon className="h-5 w-5" />
              </ListItemPrefix>
              ChatBot
            </ListItem>
            <ListItem>
              <ListItemPrefix>
                <PowerIcon className="h-5 w-5" />
              </ListItemPrefix>
              Log Out
            </ListItem>
          </List>
          <Alert open={openAlert} className="mt-auto" onClose={() => setOpenAlert(false)}>
            <CubeTransparentIcon className="mb-4 h-12 w-12" />
            <Typography variant="h6" className="mb-1">
              Upgrade to PRO
            </Typography>
            <Typography variant="small" className="font-normal opacity-80">
              For more credit join our platform at lowest rate
            </Typography>
            <div className="mt-4 flex gap-3">
              <Typography
                as="a"
                href="#"
                variant="small"
                className="font-medium opacity-80"
                onClick={() => setOpenAlert(false)}
              >
                Dismiss
              </Typography>
              <Typography as="a" href="#" variant="small" className="font-medium">
                Upgrade Now
              </Typography>
            </div>
          </Alert>
        </Card>
      </div>
    </div>
  );
}

