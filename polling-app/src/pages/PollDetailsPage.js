import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Button, List, ListItem, ListItemText, CircularProgress } from '@mui/material';
import axios from 'axios';

function PollDetailsPage() {
    const { pollId } = useParams();
    const [poll, setPoll] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchPollDetails = async () => {
            setLoading(true);
            try {
                const response = await axios.get(`/api/polls/${pollId}`); // Update with your actual API endpoint
                setPoll(response.data); // Adjust based on your API response structure
            } catch (error) {
                console.error('Failed to fetch poll details:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchPollDetails();
    }, [pollId]);

    const handleVote = async (optionId) => {
        // Placeholder for voting logic
        try {
            await axios.post(`/api/polls/${pollId}/vote`, { optionId });
            // Re-fetch poll details or update UI to reflect the new vote
        } catch (error) {
            console.error('Failed to cast vote:', error);
        }
    };

    if (loading || !poll) return <CircularProgress />;

    return (
        <div>
            <h1>{poll.question}</h1>
            <List>
                {poll.options.map((option) => (
                    <ListItem key={option.id} button onClick={() => handleVote(option.id)}>
                        <ListItemText primary={option.text} />
                    </ListItem>
                ))}
            </List>
        </div>
    );
}

export default PollDetailsPage;
