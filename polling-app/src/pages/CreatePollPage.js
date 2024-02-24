import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Updated import for react-router-dom v6
import { Button, TextField, Box } from '@mui/material';
import axios from 'axios';

function CreatePollPage() {
    const [question, setQuestion] = useState('');
    const [options, setOptions] = useState(['', '']);
    const navigate = useNavigate(); // Use useNavigate hook for navigation

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            // Attempt to post the new poll to your backend
            await axios.post('/api/polls', {
                question,
                options: options.filter(option => option.trim() !== '') // Filter out any empty options
            });
            navigate('/'); // Redirect to the home page upon successful creation
        } catch (error) {
            console.error('Failed to create poll:', error);
            // Here, you might want to set an error state and display an error message to the user
        }
    };

    // Handles updating the state for each option input field
    const handleOptionChange = (index, event) => {
        const newOptions = [...options];
        newOptions[index] = event.target.value;
        setOptions(newOptions);
    };

    // Adds a new option input field to the form
    const addOption = () => {
        setOptions([...options, '']);
    };

    return (
        <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}
        >
            <TextField
                margin="normal"
                required
                fullWidth
                label="Question"
                autoFocus
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />
            {options.map((option, index) => (
                <TextField
                    key={index}
                    margin="normal"
                    required
                    fullWidth
                    label={`Option ${index + 1}`}
                    value={option}
                    onChange={(e) => handleOptionChange(index, e)}
                />
            ))}
            <Button
                onClick={addOption}
                variant="outlined"
                sx={{ mt: 2, mb: 2 }}
            >
                Add Option
            </Button>
            <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
            >
                Create Poll
            </Button>
        </Box>
    );
}

export default CreatePollPage;
