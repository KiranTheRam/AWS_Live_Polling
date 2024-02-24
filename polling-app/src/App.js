import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import CreatePollPage from './pages/CreatePollPage';
import PollDetailsPage from './pages/PollDetailsPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} exact />
                <Route path="/create-poll" element={<CreatePollPage />} />
                <Route path="/polls/:pollId" element={<PollDetailsPage />} />
            </Routes>
        </Router>
    );
}

export default App;
