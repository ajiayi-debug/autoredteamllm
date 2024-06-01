import React, { useState } from 'react';
import axios from 'axios';
import { Container, TextField, Button, List, ListItem, ListItemText } from '@mui/material';

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSendMessage = async () => {
    if (!input) return;

    const userMessage = { sender: 'user', text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post('http://localhost:5000/chat', { message: input });
      const botMessage = { sender: 'bot', text: response.data.response };
      setMessages([...messages, userMessage, botMessage]);
    } catch (error) {
      console.error('Error fetching the bot response:', error);
    }

    setInput('');
  };

  return (
    <Container maxWidth="sm">
      <List>
        {messages.map((message, index) => (
          <ListItem key={index}>
            <ListItemText primary={message.text} />
          </ListItem>
        ))}
      </List>
      <TextField
        fullWidth
        variant="outlined"
        placeholder="Type your message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => {
          if (e.key === 'Enter') handleSendMessage();
        }}
      />
      <Button variant="contained" color="primary" onClick={handleSendMessage}>
        Send
      </Button>
    </Container>
  );
};

export default App;


