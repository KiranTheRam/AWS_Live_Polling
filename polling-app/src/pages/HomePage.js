import React, { useEffect, useState } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Button, List, ListItem, ListItemText, CircularProgress } from '@mui/material';
import axios from 'axios'; // Assuming axios is used for HTTP requests

function HomePage() {
    const [polls, setPolls] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchPolls = async () => {
            setLoading(true);
            try {
                const response = await axios.get('/api/polls'); // Update with your actual API endpoint
                setPolls(response.data.polls); // Adjust based on your API response structure
            } catch (error) {
                console.error('Failed to fetch polls:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchPolls();
    }, []);

    if (loading) return <CircularProgress />;

    return (
        <div>
            <h1>Live Polls</h1>
            <List>
                {polls.map((poll) => (
                    <ListItem key={poll.id} button component={RouterLink} to={`/polls/${poll.id}`}>
                        <ListItemText primary={poll.question} />
                    </ListItem>
                ))}
            </List>
            <Button variant="contained" color="primary" component={RouterLink} to="/create-poll">
                Create a New Poll
            </Button>
        </div>
    );
}

export default HomePage;
