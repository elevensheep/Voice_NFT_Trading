require("dotenv").config();
const express = require("express");
const cors = require('cors');
const { dbConnection } = require("./utils/db");
const config = require('./config');

// Import routes
const authRoutes = require('./auth/routes/auth.routes');
const marketplaceRoutes = require('./marketplace/api/routes/marketplace.routes');
const userRoutes = require('./auth/routes/user.routes');
const voiceRoutes = require('./voice/routes/voice.routes');

// Import middleware
const errorHandler = require('./middleware/errorHandler');

// Import Swagger configuration
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('./utils/swagger');

const app = express();

// CORS configuration
app.use(cors(config.cors));

// Body parsing middleware
app.use(express.json({ limit: config.upload.maxFileSize }));
app.use(express.urlencoded({ extended: true, limit: config.upload.maxFileSize }));

// Swagger documentation
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

// API routes
app.use("/api/auth", authRoutes);
app.use("/api/marketplace", marketplaceRoutes);
app.use("/api/user", userRoutes);
app.use("/api/voice", voiceRoutes);

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ 
    status: 'OK', 
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ 
    success: false, 
    message: 'Route not found' 
  });
});

// Global error handler
app.use(errorHandler);

// Initialize server
const startServer = async () => {
  try {
    // Validate configuration
    config.validateConfig();
    
    // Connect to database
    await dbConnection.connect();
    
    // Start server
    const PORT = config.server.port;
    app.listen(PORT, () => {
      console.log(`🚀 Server running on http://localhost:${PORT}`);
      console.log(`📚 API Documentation: http://localhost:${PORT}/api-docs`);
      console.log(`🌍 Environment: ${config.server.env}`);
    });
  } catch (error) {
    console.error('❌ Failed to start server:', error);
    process.exit(1);
  }
};

// Graceful shutdown
const gracefulShutdown = async (signal) => {
  console.log(`${signal} received. Shutting down gracefully...`);
  try {
    await dbConnection.disconnect();
    console.log('✅ Server shut down successfully');
    process.exit(0);
  } catch (error) {
    console.error('❌ Error during shutdown:', error);
    process.exit(1);
  }
};

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

// Start the server
startServer();
