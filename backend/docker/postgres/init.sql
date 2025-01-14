-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable full text search for multiple languages
CREATE EXTENSION IF NOT EXISTS unaccent;

-- Create custom collation for case-insensitive search
CREATE COLLATION IF NOT EXISTS case_insensitive (
    provider = icu,
    locale = 'und-u-ks-level2',
    deterministic = false
);

-- Set timezone
SET timezone = 'UTC'; 